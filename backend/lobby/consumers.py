from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from game.models import User

results = {}


class GameConsumer(WebsocketConsumer):

    def connect(self):
        results["connected"] = True

        #     # Join room group
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )

        self.accept()

    def disconnect(self, close_code):
        results["connected"] = True
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_to_clients(self, message):
        self.send(text_data=json.dumps(message))


    def send_server_response_to_client(self, action, username, room, payload):
        content = {
            'command': 'server_response',
            'action': {
                'actionType': action,
                'user': username,
                'room': room,
                'content': {
                    'user': username,
                    'room': room,
                    'content': payload
                }
            }
        }
        self.send_to_clients(content)

    def init_chat_handler(self, data):
        username = data['user']
        room = data['room']
        user, created = User.objects.get_or_create(username=username)

        if not user:
            error = 'Unable to get or create User with username: ' + username
            self.send_server_response_to_client('GAMECONSOLE_ERROR', username, room, error)

        success = 'Chatting in with success with username: ' + username
        self.send_server_response_to_client('GAMECONSOLE_MESSAGE', username, room, success)

    def selected_dice_handler(self, data):
        username = data['user']
        room = data['room']

        # [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
        payload = data['payload']

        formatted_payload = username + " rolled :" + ','.join(str(item) for innerlist in payload for item in innerlist)

        self.send_server_response_to_client('GAMECONSOLE_DECISION', username, room, formatted_payload)

        # TO DO:
        # use payload to update player_username
        # Game determine next actions: use payload to update player_username
        # Respond with client updates, so UI can be reset

    def gamelog_send_handler(self, text_data):
        player_username = text_data['user']

        # [['text entered by user']
        mud_gamelog_input = text_data['payload']

        print(mud_gamelog_input)

        # TO DO: parse mud_gamelog_input, determine command. Handle to update game state.

    commands = {
        'init_chat_request': init_chat_handler,
        'gamelog_send_request': gamelog_send_handler,
        'selected_dice_request': selected_dice_handler
    }
