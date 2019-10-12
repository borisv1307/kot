from typing import List

import backend.src.game.cards.definitions as definitions
from backend.src.game.cards.card import Card
from backend.src.game.cards.deck import Deck


class DeckHandler:
    __draw_pile: Deck = Deck()
    __discard_pile: Deck = Deck()
    __card_store: List[Card] = list()

    def __init__(self):
        self.__draw_pile.get_new_deck()
        self.__draw_pile.shuffle()
        self.fill_card_market()

    def fill_card_market(self):
        while len(self.__card_store) < definitions.CARD_STORE_SIZE:
            self.__card_store.append(self.__draw_pile.draw())

    def get_draw_pile_size(self):
        return len(self.__draw_pile)

    def get_discard_pile_size(self):
        return len(self.__discard_pile)

    def get_card_store(self):
        return self.__card_store

    def get_card_store_size(self):
        return len(self.__card_store)

    def buy_card(self, index):
        bought = self.__card_store.pop(index)
        self.fill_card_market()
        return bought

    def discard(self, card: Card):
        self.__discard_pile.append(card)


def print_deck_details():
    print("\n*****\n")
    print(deck_handler.get_draw_pile_size())
    print(deck_handler.get_discard_pile_size())
    print(deck_handler.get_card_store_size())

    for card in deck_handler.get_card_store():
        print(card.card_details_str())


deck_handler = DeckHandler()

print_deck_details()

buy = int(input("\n******\nwhich card"))

bought = deck_handler.buy_card(buy)
deck_handler.discard(bought)

print_deck_details()



