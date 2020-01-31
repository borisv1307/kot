import json
import pickle

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from game.engine.board import BoardGame
from game.models import User, GameState
from game.player.player import Player


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'room'
        self.room_group_name = 'chat_%s' % self.room_name

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

    def selected_dice_handler(self, data):
        username = data['user']
        room = data['room']

        # [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
        payload = data['payload']

        print(payload)

        print("selected_dice_handler")

        game = GameState.objects.get(room_name=room)
        # deserialize then store GameState object
        state: BoardGame = pickle.loads(game.board)

        # temp code, replace with actual usage of dice_handler code
        # TODO payload should just be a list of indexes:
        # [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
        # assuming this would be re-rolling "e,h, and 3"
        # DiceHandler expects this in the format [0,2,4]
        try:
            state.dice_handler.re_roll_dice(payload)
        except ValueError:
            # TODO handle the no re-rolls message gracefully
            pass

        # if state.is_game_active():
        #     state.end_game()
        #     print("game not active")
        # else:
        #     state.start_game()
        #     print("game is active")
        # ^temp code, replace with actual usage of dice_handler code

        # serialize then store modified GameState object
        game.board = pickle.dumps(state)
        game.save()

        # formatted_payload = username + " rolled :" + ','.join(str(item) for innerlist in payload for item in innerlist)
        #
        # self.send_server_response_to_client(username, room, formatted_payload)

    def end_turn_handler(self, data):
        # a method to end a players turn and let the next guy go
        # TODO FIX ME TO WORK!
        username = data['user']
        room = data['room']
        payload = data['payload']

        print("end_turn_handler")

        game = GameState.objects.get(room_name=room)

        state: BoardGame = pickle.loads(game.board)

        next_player: Player = state.get_next_player_turn()
        print(next_player.username)

        game.board = pickle.dumps(state)
        game.save()

        for p in state.players.players:
            print(p.username)

        print("next player: " + next_player.username)
        # print(state.players.current_player.username)

        # TODO self.actually_send_this_end_of_turn_to_the_UI_somehow
        if next_player is not None:
            self.send_begin_turn_response_to_client(username, room, next_player.username)
        else:
            self.send_begin_turn_response_to_client(username, room, "None")

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

    def roll_dice_handler(self, data):
        username = data['user']
        room = data['room']
        number_of_dice = data['payload']

        print("roll_dice_handler")

        # roll dice
        # send back to client...

        # roll dice, send back to client formatted:
        #   [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]

        # TEMPORARY..
        rolled_dice = [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]

        self.send_rolls_to_client(username, room, rolled_dice)
        pass

    commands = {
        'init_user_request': init_chat_handler,
        'gamelog_send_request': gamelog_send_handler,
        'selected_dice_request': selected_dice_handler,
        'roll_dice_request': roll_dice_handler,
        'end_turn_request': end_turn_handler
    }
