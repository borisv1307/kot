import json
from typing import List

import game.values.constants as constants
from game.cards.card import Card
from game.cards.discard_card import DiscardCard
from game.cards.keep_card import KeepCard
from game.deck.deck import Deck
from game.player.player import Player

from game.cards.keep_cards.victory_point_manipulation_cards.dedicated_news_team import DedicatedNewsTeam


class DeckHandler:
    """
    DeckHandler manages the draw, discard, and store pile interactions.

    Use this to purchase power cards_old_dir from the store and discard used cards_old_dir.
    creating a DeckHandler object automatically populates the draw pile from the kot_cards.json.
    The draw pile is automatically re-populated with discarded cards_old_dir upon running out.
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

    def json_store(self):
        json_data = []
        for card in self.store:
            json_data.append(card.to_dict())
        return json.dumps(json_data)

    def get_top_draw_pile_card(self):
        # if draw pile is empty, shuffle the discard pile to become draw pile
        if (len(self.draw_pile)) <= 0:
            # if discard pile is also empty, raise exception
            if len(self.discard_pile) <= 0:
                raise Exception(constants.OUT_OF_CARDS_MSG)
            self.shuffle_discard_pile_to_draw_pile()
        self.__card_store.append(self.__draw_pile.draw_from())

    def __fill_card_store(self):
        while len(self.__card_store) < constants.CARD_STORE_SIZE_LIMITER:
            self.get_top_draw_pile_card()

    def shuffle_discard_pile_to_draw_pile(self):
        self.__discard_pile.shuffle()
        while len(self.discard_pile) > 0:
            self.__draw_pile.append(self.discard_pile.draw_from())
        self.__discard_pile.clear()

    def buy_card_from_store(self, index, purchasing_player: Player):
        card_to_buy: Card = self.__card_store[index]
        if purchasing_player.energy < card_to_buy.cost:
            raise Exception(constants.INSUFFICIENT_FUNDS_MSG)
        else:
            purchasing_player.update_energy_by(-card_to_buy.cost)
            if isinstance(card_to_buy, DiscardCard):
                print("{} is a discard card".format(card_to_buy.name))
                self.discard(card_to_buy)
            elif isinstance(card_to_buy, KeepCard):
                if purchasing_player.has_instance_of_card(DedicatedNewsTeam()):
                    DedicatedNewsTeam.special_effect(purchasing_player, [])
                purchasing_player.add_card(card_to_buy)
            else:
                print("UNEXPECTED CARD TYPE!!!")
                raise Exception
            self.__card_store.remove(card_to_buy)
            self.__fill_card_store()
        return card_to_buy

    # optional second arg allows discard to handle removing card from origin as well
    def discard(self, card: Card, card_from_location: List[Card] = None):
        self.__discard_pile.append(card)
        if card_from_location is not None:
            card_from_location.remove(card)

    def sweep_store(self, player_invoking_sweep: Player):
        if player_invoking_sweep.energy < constants.SWEEP_CARD_STORE_COST:
            raise Exception(constants.INSUFFICIENT_FUNDS_TO_SWEEP_MSG)
        else:
            player_invoking_sweep.update_energy_by(
                -constants.SWEEP_CARD_STORE_COST)
            for _ in range(3):
                self.discard(self.store.pop())
            self.__fill_card_store()
