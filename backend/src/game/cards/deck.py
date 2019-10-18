import random
from typing import List

from backend.src.game.cards import card_json_parser
from backend.src.game.cards.card import Card


class Deck:

    def __init__(self):
        self.__card_deck: List[Card] = list()

    def __contains__(self, item):
        return self.__card_deck.__contains__(item)

    def __len__(self):
        return len(self.__card_deck)

    def get_new_deck(self):
        self.__card_deck: List[Card] = card_json_parser.get_power_card_deck()

    def shuffle(self):
        random.shuffle(self.__card_deck)

    def draw_from(self):
        return self.__card_deck.pop(0)  # take first item so appending "puts cards on the bottom of the pile"

    def append(self, card: Card):
        self.__card_deck.append(card)

    def clear(self):
        self.__card_deck.clear()
