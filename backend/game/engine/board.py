import game.dice.dice_resolver as dice_resolver
import game.values.constants as constants
from game.cards.keep_cards.energy_manipulation_cards.energy_hoarder import EnergyHoarder
from game.cards.keep_cards.energy_manipulation_cards.solar_powered import SolarPowered
from game.cards.keep_cards.victory_point_manipulation_cards.urbavore import Urbavore
from game.deck.deck_handler import DeckHandler
from game.dice.dice_handler import DiceHandler
from game.engine.player_queue import GamePlayers
from game.turn_actions.player_movement import yield_tokyo
from game.values.status import Status


class BoardGame:

    def __init__(self):
        self.players = GamePlayers()
        self.status = Status.SETUP
        self.winner = None
        self.deck_handler = DeckHandler()
        self.dice_handler = DiceHandler()

    def add_player(self, player):
        self.players.add_player_to_game(player)

    def start_game(self):
        self.players.set_player_order()
        self.players.get_current_player()
        self.status = Status.ACTIVE

    def check_if_winner(self, potential_winner):
        if (potential_winner.victory_points >= constants.VICTORY_POINTS_TO_WIN or
                self.players.is_last_player_alive(potential_winner)):
            self.winner = potential_winner
            self.end_game()
            return True
        return False

    def is_game_active(self):
        return self.status == Status.ACTIVE

    def end_game(self):
        self.status = Status.COMPLETED

    def start_turn_actions(self, active_player):
        player_dice_count = constants.DEFAULT_DICE_TO_ROLL
        player_re_roll_count = constants.DEFAULT_RE_ROLL_COUNT
        if active_player != self.players.get_current_player():
            raise Exception("It is not %s's turn" % (id(active_player)))
        # TODO, refactor to other method
        if active_player.has_instance_of_card(Urbavore()):
            Urbavore.special_effect(
                active_player, self.players.get_all_alive_players_minus_current_player())
        self.dice_handler.roll_initial(player_dice_count, player_re_roll_count)

    def re_roll(self, indexes_to_re_roll):
        self.dice_handler.re_roll_dice(indexes_to_re_roll)

    def resolve_dice(self, dice, turn_player):
        others = self.players.get_all_alive_players_minus_current_player()
        dice_resolver.dice_resolution(dice, turn_player, others)

    def post_roll_actions(self, active_player):
        self.resolve_dice(active_player)

        # TODO, refactor to other method
        if active_player.has_instance_of_card(EnergyHoarder()):
            EnergyHoarder.special_effect(
                active_player, self.players.get_all_alive_players_minus_current_player())
        if active_player.has_instance_of_card(SolarPowered()):
            SolarPowered.special_effect(
                active_player, self.players.get_all_alive_players_minus_current_player())
        self.check_if_winner(active_player)

    def get_next_player_turn(self):
        if self.is_game_active():
            self.players.get_next_player()
            return self.players.current_player

    def yield_tokyo_to_current_player(self, yielding_player):
        yield_tokyo(yielding_player, self.players.current_player)
