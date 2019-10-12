from typing import List
import random

from backend.src.game.cards.card import Card
from backend.src.game.cards import card_json_parser


class Deck:
    __card_deck: List[Card] = list()

    def get_new_deck(self):
        self.__card_deck = card_json_parser.get_power_card_deck()

    def shuffle(self):
        shuffled_deck: List[Card] = list()
        while len(self.__card_deck) > 0:
            i = random.randint(0, len(self.__card_deck) - 1)
            shuffled_deck.append(self.__card_deck.pop(i))
        self.__card_deck = shuffled_deck

    def __len__(self):
        return len(self.__card_deck)

    def draw(self):
        return self.__card_deck.pop()

    def append(self, card: Card):
        self.__card_deck.append(card)
