import random
from enum import Enum


class DieValue(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    ATTACK = 4
    HEAL = 5
    ENERGY = 6

    def serialize_kot_obj(self):
        return dict(die_val=self.name)


def roll() -> str:
    return random.choice(list(DieValue))


def roll_many(num: int) -> [str]:
    return [roll() for _ in range(num)]
