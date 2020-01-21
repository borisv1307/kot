from channels.generic.websocket import WebsocketConsumer
import json


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print(message)

        self.send(text_data=json.dumps({
            'message': message
        }))

    def randomcards_deck_handler(self, data):
        username = data['user']
        room = data['room']
        cards_required = data['payload']
        self.send_server_response_to_client('GAMECONSOLE_DECISION', username, room, cards)

    commands = {
        'randomcards_send_request': randomcards_deck_handler
        #To modify the command with backend class that handles this
    }