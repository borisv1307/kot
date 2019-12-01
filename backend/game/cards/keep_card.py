from abc import abstractmethod

from game.cards.card import Card


class KeepCard(Card):
    @abstractmethod
    def immediate_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError

    def special_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError
