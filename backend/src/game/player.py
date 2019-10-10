"""
This is a class that keeps the state of a given player for the game King of
Tokyo.
Locations that the player can be:
    - Outside: Denotes that the player is not on the game board.
    - Tokyo: The player is in Tokyo
"""
from backend.src.game.locations import Locations


class Player:
    def __init__(self):
        self.default_health = 10
        self.location = Locations.OUTSIDE

    def move_to_tokyo(self):
        self.location = Locations.TOKYO

    def leave_tokyo(self):
        self.location = Locations.OUTSIDE
