import json

from channels.generic.websocket import WebsocketConsumer

from backend.game.engine.board import BoardGame


class GameConsumer(WebsocketConsumer):
    master_game_controller = BoardGame()

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

    def get_the_three_store_cards(self):
        card_market = self.master_game_controller.deck_handler.store
        # card_market is now a list of three random cards, modify as needed
        card1 = card_market[0]
        card2 = card_market[1]
        card3 = card_market[2]
        return card_market

    commands = {
        'randomcards_send_request': randomcards_deck_handler
    }


# This test is temporary to prove the GameConsumer has access to the card store
def test_get_store_cards():
    game = GameConsumer(WebsocketConsumer("test"))
    three_cards = game.get_the_three_store_cards()
    print(
        "\n\tCARD 1:{}\n\tCARD 2:{}\n\tCARD 3:{}".format(three_cards[0].name, three_cards[1].name, three_cards[2].name))
    assert len(three_cards) == 3
