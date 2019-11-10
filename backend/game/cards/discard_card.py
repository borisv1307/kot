from abc import abstractmethod

from game.cards.new_card import NewCard


class DiscardCard(NewCard):
    @abstractmethod
    def immediate_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError
