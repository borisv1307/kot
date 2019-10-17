from abc import ABC


class NewCard(ABC):
    def __init__(self, name, cost, effect, footnote):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.footnote = footnote
