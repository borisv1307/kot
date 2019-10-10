from backend.src.game import constants
from backend.src.game.locations import Locations


class Player:
    def __init__(self):
        self.maximum_health = constants.DEFAULT_HEALTH
        self.current_health = self.maximum_health
        self.location = Locations.OUTSIDE
        self.is_alive = bool(0)
        self.victory_points = constants.ZERO

    def move_to_tokyo(self):
        self.location = Locations.TOKYO

    def leave_tokyo(self):
        self.location = Locations.OUTSIDE

    def change_health(self, change_integer):
        self.current_health += change_integer
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.current_health <= constants.ZERO:
            self.is_alive = bool(1)

    def change_victory_points(self, change_integer):
        self.victory_points += change_integer
        if self.victory_points < constants.ZERO:
            self.victory_points = constants.ZERO
