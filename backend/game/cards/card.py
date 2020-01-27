from abc import ABC


class Card(ABC):
    def __init__(self, name, cost, effect, footnote=None):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.footnote = footnote

    # Card is a user defined object. Provided comparison context other than object reference.
    def __eq__(self, other):
        return self is other or self.name == other.name
