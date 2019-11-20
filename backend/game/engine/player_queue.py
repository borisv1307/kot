import itertools


class GamePlayers():

    def __init__(self):
        self.all_players = []
        self.dead_players = []
        self.alive_players = []
        self.current_player = None

    def _add_initial_player(self, player):
        self.all_players.append(player)

    def _remove_initial_player(self, player):
        if player in self.all_players:
            self.all_players.remove(player)

    def set_player_order(self):
        # TODO: set this based off of dice roll minigame
        # Currently just the order in which they were added to the list
        self.alive_players = self.all_players
        self.player_cycle = itertools.cycle(self.all_players)

    def get_current_player(self):
        if not self.current_player:
            self.get_next_player()
        return self.current_player

    def get_next_player(self):
        self.current_player = self._cycle_next_alive_player()

    def get_alive_player(self):
        return self.alive_players

    def get_all_other_alive_player(self):
        return [player for player in self.alive_players if
                self.current_player != player]

    def _cycle_next_alive_player(self):
        for player in self.player_cycle:
            if player in self.alive_players:
                return player
            elif not self.alive_players:
                return None
