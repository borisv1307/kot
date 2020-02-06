import json
import pickle

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from game.cards.card import Card
from game.dice.dice_resolver import dice_resolution
from game.engine.board import BoardGame
from game.engine.dice_msg_translator import decode_selected_dice_indexes, dice_values_message_create
from game.models import User, GameState
from game.player.player import Player
from game.values import constants
from game.values.constants import DEFAULT_DICE_TO_ROLL, DEFAULT_RE_ROLL_COUNT


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'kot_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # leave group room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_group_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'group_message',
                'message': message
            }
        )

    # Receive message from room group
    def group_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))

    def create_send_response_to_client(self, command, username, room, payload):
        content = {
            'command': command,
            'action': {
                'user': username,
                'room': room,
                'content': payload
            }
        }
        return content

    def send_begin_turn_response_to_client(self, username, room, payload):
        content = self.create_send_response_to_client('begin_turn_response', username, room, payload);
        self.send_group_message(content)

    def send_server_response_to_client(self, username, room, payload):
        content = self.create_send_response_to_client('server_response', username, room, payload);
        self.send_group_message(content)

    def send_rolls_to_client(self, username, room, payload):
        content = self.create_send_response_to_client('dice_rolls_response', username, room, payload);
        self.send_group_message(content)

    def get_or_create_user(self, username, room):
        user, created = User.objects.get_or_create(username=username)

        if not user:
            error = 'Unable to get or create User with username: ' + username
            self.send_server_response_to_client(username, room, error)

        success = 'Chatting in with success with username: ' + username
        self.send_server_response_to_client(username, room, success)
        return user

    def get_or_create_game(self, username, room):
        game, created = GameState.objects.get_or_create(room_name=room)

        if not game:
            error = 'Unable to get or create Game with room: ' + room
            self.send_server_response_to_client(username, room, error)

        success = 'Chatting in with success within room: ' + room
        self.send_server_response_to_client(username, room, success)
        return game

    def init_chat_handler(self, data):
        username = data['user']
        room = data['room']
        # self.get_or_create_user(username, room)
        self.get_or_create_game(username, room)

        print("init_chat_handler")

        game = GameState.objects.get(room_name=room)
        if not game.board:
            state = BoardGame()
        else:
            state = pickle.loads(game.board)

        player: Player = Player(username)
        state.add_player(player)

        # hack to start game after 2 players join
        temp_max_players = 2
        if len(state.players.players) == temp_max_players:
            state.start_game()
            self.send_server_response_to_client(username, room, "Game started..")
            state.dice_handler.roll_initial(DEFAULT_DICE_TO_ROLL, DEFAULT_RE_ROLL_COUNT)
            self.send_begin_turn_response_to_client(username, room, state.players.get_current_player().username)
            print("Game started..")
        else:
            msg = "Joined, waiting on additional players"
            self.send_server_response_to_client(username, room, username + msg)
            print(msg)
        # hack to start game after 2 players join

        game.board = pickle.dumps(state)
        game.save()

        # success = 'Chatting in with success with username: ' + username
        # self.send_server_response_to_client(username, room, success)

    def return_dice_state_handler(self, data):
        username = data['user']
        room = data['room']

        game = GameState.objects.get(room_name=room)
        # deserialize then store GameState object
        state: BoardGame = pickle.loads(game.board)

        values = state.dice_handler.dice_values
        rolled_dice_ui_message = dice_values_message_create(values)

        print("return_dice_state_handler")
        print(rolled_dice_ui_message)

        self.send_rolls_to_client(username, room, rolled_dice_ui_message)

    def selected_dice_handler(self, data):
        username = data['user']
        room = data['room']

        # [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
        payload = data['payload']

        print("incoming")
        print(payload)

        print("selected_dice_handler")

        game = GameState.objects.get(room_name=room)
        # deserialize then store GameState object
        state: BoardGame = pickle.loads(game.board)

        selected_dice = decode_selected_dice_indexes(payload)

        print("the selected dice are: " + str(selected_dice))

        try:
            state.dice_handler.re_roll_dice(selected_dice)
        except ValueError:
            self.send_server_response_to_client(username, room, "{} out of rolls.".format(username))

        # serialize then store modified GameState object
        game.board = pickle.dumps(state)
        game.save()

        values = state.dice_handler.dice_values
        rolled_dice_ui_message = dice_values_message_create(values)
        self.send_rolls_to_client(username, room, rolled_dice_ui_message)

        print(rolled_dice_ui_message)

    def end_turn_handler(self, data):
        # a method to end a players turn and let the next guy go

        username = data['user']
        room = data['room']

        print("end_turn_handler")

        game = GameState.objects.get(room_name=room)

        state: BoardGame = pickle.loads(game.board)

        # TODO move to somewhere else
        dice_resolution(state.dice_handler.dice_values, state.players.get_current_player(),
                        state.players.get_all_alive_players_minus_current_player())
        self.send_server_response_to_client(username, room, "{} now has {} energy".format(username,
                                                                                          state.players.current_player.energy))

        cur_player = state.players.current_player
        print("Current player now has {} energy, {} health, and {} victory points".format(cur_player.energy,
                                                                                          cur_player.current_health,
                                                                                          cur_player.victory_points))

        next_player: Player = state.get_next_player_turn()
        print(next_player.username)

        state.dice_handler.roll_initial(DEFAULT_DICE_TO_ROLL, DEFAULT_RE_ROLL_COUNT)

        values = state.dice_handler.dice_values
        rolled_dice_ui_message = dice_values_message_create(values)

        game.board = pickle.dumps(state)
        game.save()

        # for p in state.players.players:
        #     print(p.username)

        # print("next player: " + next_player.username)
        # print(state.players.current_player.username)

        if next_player is not None:
            self.send_begin_turn_response_to_client(username, room, next_player.username)
        else:
            self.send_begin_turn_response_to_client(username, room, "None")

        self.send_rolls_to_client(next_player.username, room, rolled_dice_ui_message)

    def gamelog_send_handler(self, data):
        username = data['user']
        room = data['room']

        # [['text entered by user']
        mud_gamelog_input = data['payload']

        print("gamelog_send_handler")

        # TO DO:
        # parse mud_gamelog_input
        # apply input effects to game state

        self.send_server_response_to_client(username, room, mud_gamelog_input)

    # def roll_dice_handler(self, data):
    #     pass

    commands = {
        'init_user_request': init_chat_handler,
        'gamelog_send_request': gamelog_send_handler,
        'selected_dice_request': selected_dice_handler,
        # 'roll_dice_request': roll_dice_handler,
        'return_dice_state_request': return_dice_state_handler,
        'end_turn_request': end_turn_handler
    }


def test_get_phony_card_market():
    game = BoardGame()
    game.add_player(Player())
    game.add_player(Player())

    game.start_game()
    assert len(game.deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    return game.deck_handler.store


def test_temp_cards_to_json(cards=test_get_phony_card_market()):
    message = []
    card: Card
    for card in cards:
        message.append([card.name, card.cost, card.effect, card.footnote])
    return message
