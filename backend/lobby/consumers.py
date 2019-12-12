from channels.generic.websocket import JsonWebsocketConsumer
import pprint
import random


class GameConsumer(JsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.player_name = f"guest_{random.randint(1000,9999)}"
        self.msg_count = 0

    def connect(self):
        print(f"A new connection was made!")

        self.accept()

        self.send_json({
            'message': f"Welcome, {self.player_name}!"
        })

    def disconnect(self, close_code):
        print(f"A connection was closed with code: {close_code}")

    def receive_json(self, content, **kwargs):

        self.msg_count += 1

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(content)

        message = content['message']

        self.send_json({
            'message': f"{message}, message count: {self.msg_count}"
        })
