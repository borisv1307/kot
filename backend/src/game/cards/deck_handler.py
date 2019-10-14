from typing import List

import backend.src.game.cards.definitions as definitions
from backend.src.game.cards.card import Card
from backend.src.game.cards.deck import Deck


class DeckHandler:
    """
    DeckHandler manages the draw, discard, and store pile interactions.

    Use this to purchase power cards from the store and discard used cards.
    creating a DeckHandler object automatically populates the draw pile from the kot_cards.json.
    The draw pile is automatically re-populated with discarded cards upon running out.
    """
    __draw_pile: Deck = Deck()
    __discard_pile: Deck = Deck()
    __card_store: List[Card] = list()

    def __init__(self):
        self.store.clear()
        self.discard_pile.clear()
        self.__draw_pile.get_new_deck()
        self.__draw_pile.shuffle()
        self.__fill_card_store()

    def __len__(self):
        return len(self.draw_pile) + len(self.store) + len(self.discard_pile)

    @property
    def draw_pile(self):
        return self.__draw_pile

    @property
    def store(self):
        return self.__card_store

    @property
    def discard_pile(self):
        return self.__discard_pile

    def __fill_card_store(self):
        while len(self.__card_store) < definitions.CARD_STORE_SIZE:
            if (len(self.draw_pile)) <= 0:
                if len(self.discard_pile) <= 0:
                    raise Exception(definitions.OUT_OF_CARDS_MSG)
                self.shuffle_discard_pile_to_draw_pile()
            self.__card_store.append(self.__draw_pile.draw_from())

    def shuffle_discard_pile_to_draw_pile(self):
        self.__discard_pile.shuffle()
        while len(self.discard_pile) > 0:
            self.__draw_pile.append(self.discard_pile.draw_from())
        self.__discard_pile.clear()

    def buy_card(self, index):
        bought = self.__card_store.pop(index)
        self.__fill_card_store()
        return bought

    def discard(self, card: Card, card_from_location: List[Card] = None):
        """optional second arg allows discard to handle removing card from origin as well"""
        self.__discard_pile.append(card)
        if card_from_location is not None:
            card_from_location.remove(card)
