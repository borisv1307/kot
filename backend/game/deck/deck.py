import random
from typing import List

#from game.cards_old_dir import card_json_parser
from game.cards.card import Card
import game.cards.master_card_list as master_card_list

class Deck:

    def __init__(self):
        self.__card_deck: List[Card] = []

    def __contains__(self, item):
        return self.__card_deck.__contains__(item)

    def __len__(self):
        return len(self.__card_deck)

    def get_new_deck(self):
        self.__card_deck: List[Card] = master_card_list.get_all_cards()

    def shuffle(self):
        random.shuffle(self.__card_deck)

    def draw_from(self):
        return self.__card_deck.pop(0)  # take first item so appending "puts cards_old_dir on the bottom of the pile"

    def append(self, card: Card):
        self.__card_deck.append(card)

    def clear(self):
        self.__card_deck.clear()

    def add_card_to_deck(self, card: Card):
        self.__card_deck.append(card)


