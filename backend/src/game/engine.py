from backend.src.game.status import Status


class GameEngine():

    def __init__(self):
        self.players = []
        self.alive_players = []
        self.dead_players = []
        self.game_status = Status.GAME_OVER

    def add_player(self, player):
        self.players.append(player)

    def begin_game(self):
        self.alive_players = self.players
        self.game_status = Status.ACTIVE

    def play_game(self):
        for player in self.yield_next_player():
            self.take_turn(player)
            self.validate_if_winner(player)
            if not game_status:
                break
            self.set_dead_players()

    def take_turn(self, player):
        pass

    def validate_if_winner(self, player):
        if player.victory_points == 20:
            self.game_status = Status.GAME_OVER

    def set_dead_players(self):
        for player in self.alive_players:
            if not player.is_alive:
                self.dead_players.append(player)
                self.alive_players.remove(player)

    def yield_next_player(self):
        for player in self.alive_players:
            yield player
