"""
This is a dice module for the game King of Tokyo

The dice can have the following face values:
    - 1 - 3: These are the amount of victory points earned
    - attack: Depending on the player's location, hurts either monsters
    in or outside Tokyo
    - heal: Heals the player up to a maximum of 10 points
    - energy: Gives the player an energy cube to spend on upgrade cards
"""

import random

DICE_VALUES = ["1", "2", "3", "attack", "heal", "energy"]


def roll() -> str:
    """
    Returns back a randomly selected dice value.
    """
    return random.choice(DICE_VALUES)


def rolls(num: int) -> [str]:
    """
    Returns back a number "num" of randomly selected dice values in a list
    """
    return [roll() for _ in range(num)]
