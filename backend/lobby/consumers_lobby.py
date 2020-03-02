import json
import pickle

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from game.engine.board import BoardGame
from game.models import User, GameState
from game.player.player_status_resolver import player_status_summary_to_JSON
from lobby.consumers_common import create_send_response_to_client
from lobby.server_message_types import GAME_LIST_RESPONSE


class LobbyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'kot_lobby_%s' % self.room_name

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
        content = create_send_response_to_client(message_type, username, room, payload)
        self.send_group_message(content)

    def request_game_list(self, data):
        username = data['user']
        room = data['room']

        game = GameState.objects.all()
        rooms = {}
        for state_from_db in game:
            if state_from_db.board:
                state: BoardGame = pickle.loads(state_from_db.board)
                players_as_json = player_status_summary_to_JSON(state.players)
                rooms[state_from_db.room_name] = players_as_json

        self.send_to_client(GAME_LIST_RESPONSE, username, room, rooms)

    commands = {
        'request_game_list': request_game_list
    }
