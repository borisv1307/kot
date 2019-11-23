import itertools

from game.player.player import Player


class GamePlayers():

    def __init__(self):
        self.all_players = []
        self.current_player = None

    def _add_player_to_game(self, new_player):
        if isinstance(new_player, Player):
            self.all_players.append(new_player)
        else:
            raise TypeError("Object passed in was not an instance of Player")

    def set_player_order(self):
        self.player_cycle = itertools.cycle(self.all_players)

    def get_current_player(self):
        if not self.current_player:
            self.get_next_player()
        return self.current_player

    def get_next_player(self):
        self.current_player = self._cycle_next_alive_player()

    def get_alive_players(self):
        return [player for player in self.all_players if player.is_alive]

    def get_dead_players(self):
        return [player for player in self.all_players if not player.is_alive]

    def get_all_alive_players_minus_current_player(self):
        return [player for player in self.get_alive_players() if
                self.current_player != player]

    def if_last_player_alive(self, possible_last_player):
        return [possible_last_player] == self.players.get_alive_players()

    def _cycle_next_alive_player(self):
        for player in self.player_cycle:
            if player.is_alive:
                return player
            elif not self.get_alive_players():
                return None
