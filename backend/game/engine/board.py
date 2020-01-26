import game.dice.dice_resolver as dice_resolver

import game.values.constants as constants
from game.deck.deck_handler import DeckHandler

from game.cards.keep_cards.energy_manipulation_cards.solar_powered import SolarPowered

from game.engine.player_queue import GamePlayers
from game.values.status import Status


class BoardGame:

    def __init__(self):
        self.players = GamePlayers()
        self.status = Status.SETUP
        self.winner = None
        self.deck_handler = DeckHandler()

    def add_player(self, player):
        self.players.add_player_to_game(player)

    def start_game(self):
        self.players.set_player_order()
        self.status = Status.ACTIVE

    def check_if_winner(self, potential_winner):
        if (potential_winner.victory_points == constants.VICTORY_POINTS_TO_WIN or
                self.players.is_last_player_alive(potential_winner)):
            self.winner = potential_winner
            self.end_game()

    def end_game(self):
        self.status = Status.COMPLETED

    def turn(self, active_player):
        if active_player != self.players.get_current_player():
            raise Exception("It is not %s's turn" % (id(active_player)))
        self.turn_actions(active_player)
        if active_player.has_instance_of_card(SolarPowered()):
            SolarPowered.special_effect(active_player, self.players.get_all_alive_players_minus_current_player())
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
