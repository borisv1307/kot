import itertools

from game.cards.keep_cards.victory_point_manipulation_cards.eater_of_the_dead import EaterOfTheDead
from game.player.player import Player
from game.values.locations import Locations


class GamePlayers:

    def __init__(self):
        self.players = []
        self.current_player = None
        self.player_cycle = []

    def add_player_to_game(self, new_player):
        if not isinstance(new_player, Player):
            raise TypeError("Object passed in was not an instance of Player")
        if new_player in self.players:
            raise Exception("Player has already been added to game")
        self.players.append(new_player)

    def set_player_order(self):
        self.player_cycle = itertools.cycle(self.players)

    def get_current_player(self):
        if not self.current_player:
            self.get_next_player()
        return self.current_player

    def get_player_by_username_from_alive(self, username):
        for player in self.get_alive_players():
            if player.username == username:
                return player

    def reset_allowed_to_yield(self):
        for player in self.players:
            player.allowed_to_yield = False

    def get_next_player(self):
        self.reset_allowed_to_yield()
        if self.current_player and self.current_player.gets_bonus_turn:
            self.current_player.gets_bonus_turn = False
        else:
            self.current_player = self._cycle_next_alive_player()

    def get_alive_players(self):
        return [player for player in self.players if player.is_alive]

    def get_dead_players(self):
        return [player for player in self.players if not player.is_alive]

    def get_all_alive_players_minus_current_player(self):
        return [player for player in self.get_alive_players() if
                self.current_player != player]

    def is_last_player_alive(self, possible_last_player):
        return [possible_last_player] == self.get_alive_players()

    def _cycle_next_alive_player(self):
        if not self.get_alive_players():
            raise Exception("There are no alive players left")
        for player in self.player_cycle:
            if player.is_alive:
                return player

    def get_count_in_tokyo_ignore_current_player(self):
        return len([player for player in self.get_all_alive_players_minus_current_player() if
                    player.location != Locations.OUTSIDE])

    def check_for_eater_of_dead_holders(self):
        return [player for player in self.get_alive_players() if player.has_instance_of_card(EaterOfTheDead())]

    def check_for_newly_dead_players(self):
        return [player for player in self.players if player.is_newly_dead]

    def apply_eater_of_dead_action(self):
        card_holders = self.check_for_eater_of_dead_holders()
        newly_dead = self.check_for_newly_dead_players()
        for _ in newly_dead:
            for player in card_holders:
                EaterOfTheDead().special_effect(player)
