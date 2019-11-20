
import game.dice.dice_resolver as dice_resolver
from game.engine.player_queue import GamePlayers
import game.values.constants as constants
import game.values.status as status


class BoardGame():

    def __init__(self):
        self.players = GamePlayers()
        self.STATUS = status.SETUP
        self.WINNER = None

    def start_game(self):
        self.players.set_player_order()
        self.STATUS = status.ACTIVE

    def check_if_winner(self, player):
        if player.victory_points == constants.VICTORY_POINTS_TO_WIN or all(
                alive_player == player for alive_player
                in self.players.get_alive_player()):
            self.WINNER = player
            self.end_game()

    def end_game(self):
        self.STATUS = status.COMPLETED

    def turn(self, current_player):
        # roll dice & dice_resoultion method
        pass

    def is_game_active(self):
        if self.STATUS == status.ACTIVE:
            return True
        else:
            return False

    def play_game(self):
        while self.is_game_active():
            current_player = self.players.get_current_player()
            self.turn(current_player)
            self.check_if_winner(current_player)
