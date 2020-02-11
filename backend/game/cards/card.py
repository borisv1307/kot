import json
from abc import ABC

from game.values.constants import CARD_NAME_KEY, CARD_COST_KEY, CARD_EFFECT_KEY, CARD_FOOTNOTE_KEY


class Card(ABC):
    def __init__(self, name, cost, effect, footnote=None):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.footnote = footnote

    # Card is a user defined object. Provided comparison context other than object reference.
    def __eq__(self, other):
        return self is other or self.name == other.name

    def to_dict(self):
        return {
            CARD_NAME_KEY: self.name,
            CARD_COST_KEY: self.cost,
            CARD_EFFECT_KEY: self.effect,
            CARD_FOOTNOTE_KEY: self.footnote
        }

    def to_json(self):
        return json.dumps(self.to_dict())
