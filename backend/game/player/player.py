from typing import List

from game.cards.card import Card
from game.values import constants
from game.values.locations import Locations


class Player:
    def __init__(self):
        self.maximum_health = self.current_health = constants.DEFAULT_HEALTH
        self.location = Locations.OUTSIDE
        self.is_alive = True
        self.victory_points = constants.DEATH_HIT_POINT
        self.energy = constants.DEFAULT_ENERGY_CUBE
        self.cards: List[Card] = []

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

    def update_max_health_by(self, change_integer):
        self.maximum_health += change_integer
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.maximum_health < constants.DEATH_HIT_POINT:
            self.maximum_health = constants.DEATH_HIT_POINT

    def update_victory_points_by(self, change_integer):
        self.victory_points += change_integer
        if self.victory_points < constants.DEATH_HIT_POINT:
            self.victory_points = constants.DEATH_HIT_POINT

    def update_energy_by(self, change_integer):
        self.energy += change_integer
        if self.energy < constants.DEFAULT_ENERGY_CUBE:
            self.energy = constants.DEFAULT_ENERGY_CUBE

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def has_instance_of_card(self, card: Card):
        for player_card in self.cards:
            if type(player_card) == type(card):
                return True
        return False

    def discard_all_cards(self):
        self.cards.clear()

    def lose_all_stars(self):
        self.victory_points = constants.DEATH_HIT_POINT
