import random
from enum import Enum


class DieValue(Enum):
    ONE = 0
    TWO = 1
    THREE = 2
    ATTACK = 3
    HEAL = 4
    ENERGY = 5


def roll() -> str:
    return random.choice(list(DieValue))


def roll_many(num: int) -> [str]:
    return [roll() for _ in range(num)]
