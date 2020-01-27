from django.conf import settings
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import django
import os

from game.models import User
from backend.game.engine.board import BoardGame


class GameConsumer(WebsocketConsumer):
    master_game_controller = BoardGame()

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
        status = self.commands[data['command']](self, data)

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

    def send_server_response_to_client(self, username, room, payload):
        content = {
            'command': 'server_response',
            'action': {
                'user': username,
                'room': room,
                'content': payload
            }
        }
        self.send_group_message(content)

    def init_chat_handler(self, data):
        username = data['user']
        room = data['room']
        user, created = User.objects.get_or_create(username=username)

        if not user:
            error = 'Unable to get or create User with username: ' + username
            self.send_server_response_to_client(username, room, error)

        success = 'Chatting in with success with username: ' + username
        self.send_server_response_to_client(username, room, success)

    def selected_dice_handler(self, data):
        username = data['user']
        room = data['room']

        print("selected dice handler")

        # [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
        payload = data['payload']

        formatted_payload = username + " rolled :" + ','.join(str(item) for innerlist in payload for item in innerlist)

        self.send_server_response_to_client(username, room, formatted_payload)

        # TO DO:
        # use payload to update 'user'
        # Game determine next actions: use payload to update player_username
        # Respond with client updates, so UI can be reset

    def gamelog_send_handler(self, data):
        username = data['user']
        room = data['room']

        # [['text entered by user']
        mud_gamelog_input = data['payload']

        # TO DO:
        # parse mud_gamelog_input
        # apply input effects to game state

        self.send_server_response_to_client(username, room, mud_gamelog_input)

    def selected_card_handler(self, data):
        username = data['user']
        room = data['room']

        print("selected card handler")

        payload = data['payload']

        self.send_server_response_to_client(username, room, payload)

    def get_the_three_store_cards(self):
        card_market = self.master_game_controller.deck_handler.store
        # card_market is now a list of three random cards, modify as needed
        card1 = card_market[0]
        card2 = card_market[1]
        card3 = card_market[2]
        return card_market

    # This test is temporary to prove the GameConsumer has access to the card store
    def test_get_store_cards():
        game = GameConsumer(WebsocketConsumer("test"))
        three_cards = game.get_the_three_store_cards()
        print(
            "\n\tCARD 1:{}\n\tCARD 2:{}\n\tCARD 3:{}".format(three_cards[0].name, three_cards[1].name, three_cards[2].name))
        assert len(three_cards) == 3
    
    commands = {
        'init_user_request': init_chat_handler,
        'gamelog_send_request': gamelog_send_handler,
        'selected_dice_request': selected_dice_handler,
        'send_cards_request': get_the_three_store_cards

    }
