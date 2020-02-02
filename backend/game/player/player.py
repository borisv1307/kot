import random
from typing import List

from game.cards.card import Card
from game.values import constants
from game.values.locations import Locations


class Player:
    def __init__(self, username=None):
        if username is None:
            self.username = "guest_{}".format(random.randint(1000, 9999))
        else:
            self.username = username
        self.maximum_health = self.current_health = constants.DEFAULT_HEALTH
        self.location = Locations.OUTSIDE
        self.is_alive = True
        self.victory_points = constants.DEATH_HIT_POINT
        self.energy = constants.DEFAULT_ENERGY_CUBE
        self.cards: List[Card] = []

    def __eq__(self, other):
        return isinstance(other, Player) and self.username == other.username

    def move_to_tokyo(self):
        self.location = Locations.TOKYO

    def leave_tokyo(self):
        self.location = Locations.OUTSIDE

    def update_health_by(self, change_integer):
        self.current_health += change_integer
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.current_health <= 0:
            self.is_alive = False

    def update_max_health_by(self, change_integer):
        self.maximum_health += change_integer
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.maximum_health < 0:
            self.maximum_health = 0

    def update_victory_points_by(self, change_integer):
        self.victory_points += change_integer
        if self.victory_points < 0:
            self.victory_points = 0

    def update_energy_by(self, change_integer):
        self.energy += change_integer
        if self.energy < constants.DEFAULT_ENERGY_CUBE:
            self.energy = constants.DEFAULT_ENERGY_CUBE

    def lose_all_stars(self):
        self.victory_points = 0

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
