
import game.dice.dice_resolver as dice_resolver
from game.cards.keep_cards.energy_manipulation_cards.energy_hoarder import EnergyHoarder
from game.engine.player_queue import GamePlayers
from game.values.status import Status
import game.values.constants as constants


class BoardGame():

    def __init__(self):
        self.players = GamePlayers()
        self.status = Status.SETUP
        self.winner = None

    def start_game(self):
        self.players.set_player_order()
        self.status = Status.ACTIVE

    def check_if_winner(self, potential_winner):
        if (potential_winner.victory_points == constants.VICTORY_POINTS_TO_WIN or
                players.is_last_player_alive(potential_winner)):
            self.winner = potential_winner
            self.end_game()

    def end_game(self):
        self.status = Status.COMPLETED

    def turn(self, active_player):
        if active_player != self.players.get_current_player():
            raise Exception("It is not %s's turn" % (id(active_player)))
        self.turn_actions(active_player)
        if active_player.has_instance_of_card(EnergyHoarder()):
            EnergyHoarder.special_effect(active_player, self.players.get_all_alive_players_minus_current_player())
        self.check_if_winner(active_player)

    def is_game_active(self):
        return self.status == Status.ACTIVE

    def turn_actions(self, dice, turn_player):
        others = self.players.get_all_alive_players_minus_current_player()
        dice_resolver.dice_resolution(dice, turn_player, others)

    def get_next_player_turn(self):
        if self.is_game_active():
            self.players.get_next_player()
            return self.players.current_player
