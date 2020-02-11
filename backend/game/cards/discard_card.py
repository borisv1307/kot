from abc import abstractmethod

from game.cards.card import Card


class DiscardCard(Card):
    def __init__(self, name, cost, effect, footnote=None):
        super().__init__(name, cost, effect, footnote)
        self.type = "Discard"

    @abstractmethod
    def immediate_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError
