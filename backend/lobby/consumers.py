from django.conf import settings
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import django
import os

from game.models import User

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        status = self.commands[data['command']](self, data)

    def send_to_clients(self, message):
        self.send(text_data=json.dumps(message))

    def send_server_response_to_client(self, username, room, payload):
        content = {
            'command': 'server_response',
            'action': {
                'user': username,
                'room': room,
                'content': payload
            }
        }
        self.send_to_clients(content)

    def init_chat_handler(self, data):
        username = data['user']
        room = data['room']
        user, created = User.objects.get_or_create(username=username)

        if not user:
            error = 'Unable to get or create User with username: ' + username
            self.send_server_response_to_client(username, room, error)

        success = 'Chatting in with success with username: ' + username
        self.send_server_response_to_client(username, room, success)

        return success

    def selected_dice_handler(self, data):
        # Placeholder... to avoid nullptr when UI sends 'selected_dice'
        return False

    commands = {
        'init_user_request': init_chat_handler,
        'selected_dice': selected_dice_handler
    }
