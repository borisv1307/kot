from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class GameConsumer(WebsocketConsumer):

    def connect(self):

        #     # Join room group
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_to_clients(self, message):
        self.send(text_data=json.dumps(message))

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def selected_dice(self, text_data):
        player_username = text_data['from']

        # [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
        payload = text_data['payload']

        print(player_username)
        print(payload)

        # TO DO:
        # use payload to update player_username
        # Game determine next actions: use payload to update player_username
        # Respond with client updates, so UI can be reset

    def create_message_json(self, id, username, gameroom, content):
        return {
            'id': str(id),
            'user': username,
            'game_session_id': gameroom,
            'content': content
        }

    def gamelog_send(self, text_data):
        player_username = text_data['from']

        # [['text entered by user']
        mud_gamelog_input = text_data['payload']

        print(mud_gamelog_input)

        # TO DO: parse mud_gamelog_input, determine command. Handle to update game state.

        content = {
            'command': 'server_response',
            'message': self.create_message_json(1, player_username, 'HRoom_1234', mud_gamelog_input)
        }

        # self.send(text_data=json.dumps({
        #     'payload': mud_gamelog_input
        # }))

        self.send_to_clients(content)

    commands = {
        'gamelog_send': gamelog_send,
        'selected_dice': selected_dice
    }
