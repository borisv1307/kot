"""
This is a dice class for the game King of Tokyo

The dice can have the following face values:
    - 1 - 3: These are the amount of victory points earned
    - attack: Depending on the player's location, hurts either monsters
    in or outside Tokyo
    - heal: Heals the player up to a maximum of 10 points
    - energy: Gives the player an energy cube to spend on upgrade cards
"""

import random


class Dice:
    def __init__(self):

        self.values = ["1", "2", "3", "attack", "heal", "energy"]

        return

    def roll(self) -> str:
        return random.choice(self.values)
