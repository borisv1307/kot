from abc import abstractmethod

from game.cards.card import Card


class DiscardCard(Card):
    def immediate_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError
