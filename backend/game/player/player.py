from game.values import constants
from game.values.locations import Locations


# from game.cards.card import Card


class Player:
    def __init__(self):
        self.maximum_health = self.current_health = constants.DEFAULT_HEALTH
        self.location = Locations.OUTSIDE
        self.is_alive = True
        self.victory_points = constants.DEATH_HIT_POINT
        self.energy = constants.DEFAULT_ENERGY_CUBE
        self.card_on_hand = {}

    def move_to_tokyo(self):
        self.location = Locations.TOKYO

    def leave_tokyo(self):
        self.location = Locations.OUTSIDE

    def update_health_by(self, change_integer):
        self.current_health += change_integer
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.current_health <= constants.DEATH_HIT_POINT:
            self.is_alive = False

    def update_victory_points_by(self, change_integer):
        self.victory_points += change_integer
        if self.victory_points < constants.DEATH_HIT_POINT:
            self.victory_points = constants.DEATH_HIT_POINT

    def update_energy_by(self, change_integer):
        self.energy += change_integer
        if self.energy < constants.DEFAULT_ENERGY_CUBE:
            self.energy = constants.DEFAULT_ENERGY_CUBE

    def add_keep_card(self, card):
        self.card_on_hand[card.name] = card.effect

    def remove_keep_card(self, card):
        self.card_on_hand.pop(card.name)
