from abc import abstractmethod

from game.cards.card import Card
from game.player import Player


class KeepCard(Card):
    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.add_card(self, card)

    @abstractmethod
    def special_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError
