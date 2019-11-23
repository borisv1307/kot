
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

    def check_if_winner(self, potential_winner):
        if (potential_winner.victory_points == constants.VICTORY_POINTS_TO_WIN or
                players.if_last_player_alive(potential_winner)):
            self.WINNER = potential_winner
            self.end_game()

    def end_game(self):
        self.STATUS = status.COMPLETED

    def turn(self, active_player):
        if active_player == self.players.get_current_player():
            self.turn_actions(active_player)
            self.check_if_winner(active_player)
        else:
            # TODO player object should have a name property here
            raise Exception("It is not %s's turn" % (id(active_player)))

    def is_game_active(self):
        return self.STATUS == status.ACTIVE

    def turn_actions(self, turn_player):
        # roll dice & dice_resoultion method
        pass
