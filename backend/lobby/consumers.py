import json
import pickle

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from game.dice.dice_resolver import dice_resolution
from game.engine.board import BoardGame
from game.engine.dice_msg_translator import decode_selected_dice_indexes, dice_values_message_create
from game.irepository.irepository_game import IRepositoryGame
from game.irepository.irepository_player import IRepositoryPlayer
from game.irepository.irepository_dice import IRepositoryDice
from game.irepository.irepository_play import IRepositoryPlay
from game.models import User, GameState
from game.player.player import Player
from game.player.player_status_resolver import player_status_summary_to_JSON
from game.values.constants import DEFAULT_RE_ROLL_COUNT
from game.values.exceptions import InsufficientFundsException
from lobby.consumers_common import save_game, reconstruct_game, create_send_response_to_client
from lobby.server_message_types import PLAYER_STATUS_UPDATE_RESPONSE, BEGIN_TURN_RESPONSE, SERVER_RESPONSE, \
    DICE_ROLLS_RESPONSE, CARD_STORE_RESPONSE, YIELD_ALERT, END_TURN, WINNER_ALERT


def dice_vals_log_message(player_name, values):
    msg = "{} rolled: {}".format(
        player_name, ", ".join([val.name for val in values]))
    return msg


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

    def send_to_client(self, message_type, username, room, payload):
        content = create_send_response_to_client(
            message_type, username, room, payload)
        self.send_group_message(content)

    def get_or_create_user(self, username, room):
        user, created = User.objects.get_or_create(username=username)

        if not user:
            error = 'Unable to get or create User with username: ' + username
            self.send_to_client(SERVER_RESPONSE, username, room, error)

        success = 'Chatting in with success with username: ' + username
        self.send_to_client(SERVER_RESPONSE, username, room, success)
        return user

    def get_or_create_game(self, username, room):
        game, created = GameState.objects.get_or_create(room_name=room)
        i_repository_game = IRepositoryGame()
        i_repository_player = IRepositoryPlayer()

        if not i_repository_game.get_game_by_room(room):
            game_store = i_repository_game.save_game(room)
        else:
            error = 'Room already exist in analytics database, Unable to create Game with room: ' + room

        if not i_repository_player.get_players_by_username_and_room(username, room):
            player_store = i_repository_player.save_player(username, room)
        else:
            error = 'Player in this room already exist in analytics database, Unable to create Player in room: ' + room

        if not game:
            error = 'Unable to get or create Game with room: ' + room
            self.send_to_client(SERVER_RESPONSE, username, room, error)

        success = 'Chatting in with success within room: ' + room
        self.send_to_client(SERVER_RESPONSE, username, room, success)
        return game

    def start_web_game(self, room, state, username):
        state.start_game()
        self.send_to_client(SERVER_RESPONSE, username, room, "Game started..")
        state.dice_handler.roll_initial(
            state.players.current_player.dice_allowed, DEFAULT_RE_ROLL_COUNT)
        self.send_to_client(CARD_STORE_RESPONSE, username,
                            room, state.deck_handler.json_store())
        self.send_to_client(BEGIN_TURN_RESPONSE, username,
                            room, state.players.get_current_player().username)
        print("Game started..")

    def init_chat_handler(self, data):
        username = data['user']
        room = data['room']

        self.get_or_create_game(username, room)

        game = GameState.objects.get(room_name=room)
        if not game.board:
            state = BoardGame()
        else:
            state = pickle.loads(game.board)

        player: Player = Player(username)
        if player not in state.players.players and not state.is_game_active():
            # free cards to demonstrate inventory

            # player.add_card(EnergyHoarder())
            # player.add_card(SolarPowered())
            # player.add_card(EvenBigger())
            player.update_energy_by(1000)
            state.add_player(player)

        # hack to start game after 2 players join
        temp_max_players = 2
        if len(state.players.players) == temp_max_players:
            self.start_web_game(room, state, username)
        else:
            msg = "Joined, waiting on additional players"
            self.send_to_client(SERVER_RESPONSE, username,
                                room, username + msg)

        player_summaries = player_status_summary_to_JSON(state.players)
        self.send_to_client(PLAYER_STATUS_UPDATE_RESPONSE,
                            username, room, player_summaries)

        save_game(game, state)

    def return_dice_state_handler(self, data):
        username, room, game, state = reconstruct_game(data)
        i_repository_dice = IRepositoryDice()

        values = state.dice_handler.dice_values
        if len(values) == 6:
            dice_store = i_repository_dice.save_dice(username, room, values[0], values[1], values[2], values[3],
                                                     values[4], values[5], None, None, state.dice_handler.re_rolls_left,
                                                     None)

        rolled_dice_ui_message = dice_values_message_create(values)
        self.send_to_client(SERVER_RESPONSE, username, room,
                            dice_vals_log_message(username, values))
        self.send_to_client(DICE_ROLLS_RESPONSE, username,
                            room, rolled_dice_ui_message)

    def selected_dice_handler(self, data):
        username, room, game, state = reconstruct_game(data)
        i_repository_dice = IRepositoryDice()

        payload = data['payload']

        selected_dice = decode_selected_dice_indexes(payload)

        try:
            state.dice_handler.re_roll_dice(selected_dice)
            values = state.dice_handler.dice_values
            self.send_to_client(SERVER_RESPONSE, username,
                                room, dice_vals_log_message(username, values))
            rolled_dice_ui_message = dice_values_message_create(values)
            self.send_to_client(DICE_ROLLS_RESPONSE, username,
                                room, rolled_dice_ui_message)
            save_game(game, state)
        except ValueError:
            self.send_to_client(SERVER_RESPONSE, username,
                                room, "{} out of rolls.".format(username))

        # serialize then store modified GameState object
        save_game(game, state)
        values = state.dice_handler.dice_values
        if len(values) == 6:
            dice_store = i_repository_dice.save_dice(username, room, values[0], values[1], values[2], values[3],
                                                     values[4], values[5], None, None, state.dice_handler.re_rolls_left,
                                                     selected_dice)

        rolled_dice_ui_message = dice_values_message_create(values)
        self.send_to_client(DICE_ROLLS_RESPONSE, username, room, rolled_dice_ui_message)

    def end_turn_handler(self, data):
        # a method to end a players turn and let the next guy go
        username, room, game, state = reconstruct_game(data)
        state.post_roll_actions(state.players.current_player)
        player_summaries = player_status_summary_to_JSON(state.players)
        self.send_to_client(PLAYER_STATUS_UPDATE_RESPONSE,
                            username, room, player_summaries)

        next_player: Player = state.get_next_player_turn()

        state.dice_handler.roll_initial(
            state.players.current_player.dice_allowed, DEFAULT_RE_ROLL_COUNT)

        values = state.dice_handler.dice_values

        rolled_dice_ui_message = dice_values_message_create(values)

        save_game(game, state)

        if next_player:
            self.send_to_client(BEGIN_TURN_RESPONSE, username,
                                room, next_player.username)
            self.send_to_client(DICE_ROLLS_RESPONSE,
                                next_player.username, room, rolled_dice_ui_message)
            self.send_to_client(SERVER_RESPONSE, username, room,
                                dice_vals_log_message(next_player.username, values))
        else:
            self.send_to_client(BEGIN_TURN_RESPONSE, username, room, "None")

        for player in state.players.players:
            if state.check_if_winner(player):
                self.send_to_client(WINNER_ALERT, state.players.current_player.username, room, "Winner")

    def gamelog_send_handler(self, data):
        username, room, game, state = reconstruct_game(data)

        mud_gamelog_input = data['payload']

        self.send_to_client(SERVER_RESPONSE, username, room, mud_gamelog_input)

    def card_store_request_handler(self, data):

        username, room, game, state = reconstruct_game(data)
        selected_cards_ui_message = state.deck_handler.json_store()

        self.send_to_client(CARD_STORE_RESPONSE, username,
                            room, selected_cards_ui_message)

    def yield_tokyo_request_handler(self, data):
        username, room, game, state = reconstruct_game(data)
        player = state.players.get_player_by_username_from_alive(username)

        if player.allowed_to_yield:
            state.yield_tokyo_to_current_player(player)
            self.send_to_client(SERVER_RESPONSE, username, room,
                                "{} yields Tokyo to {}!".format(username, state.players.current_player.username))

            state.players.reset_allowed_to_yield()

            player_summaries = player_status_summary_to_JSON(state.players)
            self.send_to_client(PLAYER_STATUS_UPDATE_RESPONSE,
                                username, room, player_summaries)
            self.send_to_client(
                END_TURN, state.players.current_player.username, room, "allow end turn")
        else:
            print("{} can't yield tokyo!".format(username))
        save_game(game, state)

    def keep_tokyo_request_handler(self, data):
        username, room, game, state = reconstruct_game(data)
        player = state.players.get_player_by_username_from_alive(username)
        player.allowed_to_yield = False
        save_game(game, state)

        self.send_to_client(SERVER_RESPONSE, username, room,
                            "{} refuses to yield Tokyo!".format(username))
        awaiting_yield_response = False

        for p in state.players.players:
            if p.allowed_to_yield:
                awaiting_yield_response = True
                self.send_to_client(SERVER_RESPONSE, username, room,
                                    "Waiting for {} to decide whether to yield Tokyo!".format(p.username))

        if not awaiting_yield_response:
            self.send_to_client(
                END_TURN, state.players.current_player.username, room, "allow end turn")

    def resolve_dice_handler(self, data):
        username, room, game, state = reconstruct_game(data)
        self.send_to_client(SERVER_RESPONSE, username, room,
                            "{} locked in dice".format(state.players.current_player.username))

        dice_resolution(state.dice_handler.dice_values, state.players.get_current_player(),
                        state.players.get_all_alive_players_minus_current_player())

        player_summaries = player_status_summary_to_JSON(state.players)
        self.send_to_client(PLAYER_STATUS_UPDATE_RESPONSE,
                            username, room, player_summaries)

        save_game(game, state)

        self.trigger_yield_popup_if_necessary(state, room)

    def trigger_yield_popup_if_necessary(self, state, room):
        awaiting_yield_response = False

        for p in state.players.players:
            if p.allowed_to_yield:
                awaiting_yield_response = True
                self.send_to_client(SERVER_RESPONSE, state.players.current_player.username, room,
                                    "Waiting for {} to decide whether to yield Tokyo!".format(p.username))
                self.send_to_client(YIELD_ALERT, p.username, room, "yield")

        if not awaiting_yield_response:
            self.send_to_client(
                END_TURN, state.players.current_player.username, room, "allow end turn")

    def buy_card_request_handler(self, data):
        username, room, game, state = reconstruct_game(data)

        if username != state.players.current_player.username:
            return

        index_to_buy = data['payload']
        try:
            bought = state.deck_handler.buy_card_from_store(index_to_buy, state.players.current_player,
                                                            state.players.get_all_alive_players_minus_current_player())
            if bought:
                i_repository_play = IRepositoryPlay()
                i_repository_play.save_play_card_purchased(username, room, bought.name, bought.card_type,
                                                           state.players.current_player.location,
                                                           state.players.current_player.victory_points,
                                                           state.players.current_player.energy,
                                                           state.players.current_player.current_health)

            current_card_store = state.deck_handler.json_store()
            self.send_to_client(CARD_STORE_RESPONSE,
                                username, room, current_card_store)

            player_summaries = player_status_summary_to_JSON(state.players)
            self.send_to_client(PLAYER_STATUS_UPDATE_RESPONSE,
                                username, room, player_summaries)
            self.send_to_client(SERVER_RESPONSE, username, room,
                                "{} bought {}!".format(
                                    state.players.current_player.username, bought.name))
        except InsufficientFundsException:
            self.send_to_client(SERVER_RESPONSE, username, room,
                                "{} tried to buy {} but has insufficient energy!".format(
                                    username, state.deck_handler.store[index_to_buy].name)
                                )

        save_game(game, state)

    def card_store_sweep_request_handler(self, data):
        username, room, game, state = reconstruct_game(data)
        if state.players.current_player.username == username:
            cards_swept = state.deck_handler.get_top_three_cards()
            print("Cards to be swept {}".format(cards_swept))

            successfully_swept_cardstore = state.deck_handler.sweep_store(
                state.players.current_player)

            if successfully_swept_cardstore is None:
                i_repository_play = IRepositoryPlay()
                i_repository_play.save_play_card_swept(username, room, cards_swept[2].name,
                                                       cards_swept[2].card_type,
                                                       cards_swept[1].name,
                                                       cards_swept[1].card_type,
                                                       cards_swept[0].name,
                                                       cards_swept[0].card_type,
                                                       state.players.current_player.location,
                                                       state.players.current_player.victory_points,
                                                       state.players.current_player.energy,
                                                       state.players.current_player.current_health)
            cards_swept.clear()

            if not successfully_swept_cardstore:
                message = "{} does not have enough funds to sweep the card store!".format(
                    username)
                self.send_to_client(SERVER_RESPONSE, username, room, message)
        else:
            print("{} tried to sweep out of turn!".format(username))

        player_summaries = player_status_summary_to_JSON(state.players)
        self.send_to_client(PLAYER_STATUS_UPDATE_RESPONSE,
                            username, room, player_summaries)

        selected_cards_ui_message = state.deck_handler.json_store()
        self.send_to_client(CARD_STORE_RESPONSE, username,
                            room, selected_cards_ui_message)

        save_game(game, state)

    commands = {
        'init_user_request': init_chat_handler,
        'gamelog_send_request': gamelog_send_handler,
        'selected_dice_request': selected_dice_handler,
        # 'roll_dice_request': roll_dice_handler,
        'return_dice_state_request': return_dice_state_handler,
        'resolve_dice_request': resolve_dice_handler,
        'end_turn_request': end_turn_handler,
        'card_store_request': card_store_request_handler,
        'yield_tokyo_request': yield_tokyo_request_handler,
        'keep_tokyo_request': keep_tokyo_request_handler,
        'sweep_card_store_request': card_store_sweep_request_handler,
        'buy_card_request': buy_card_request_handler
    }
