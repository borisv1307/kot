from abc import ABC


class Card(ABC):
    def __init__(self, name, cost, effect, footnote=None):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.footnote = footnote

    @abstractmethod
    def immediate_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError
