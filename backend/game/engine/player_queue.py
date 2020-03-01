import itertools

from game.player.player import Player


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
