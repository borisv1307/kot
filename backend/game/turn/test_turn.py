import collections
import pytest

from game import constants
import game.turn as turn
from game.dice.dice import DieValue
from game.locations import Locations
from game.player.player import Player


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


def test_less_than_three_twos_rolled_no_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.HEAL, DieValue.ATTACK,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 0


def test_three_twos_rolled_two_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.HEAL,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 2


def test_four_twos_rolled_three_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 3


def test_five_threes_rolled_five_victory_points_awarded():
    dice = collections.Counter([DieValue.THREE, DieValue.THREE,
                                DieValue.THREE, DieValue.THREE,
                                DieValue.THREE, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 5


def test_six_ones_rolled_four_victory_points_awarded():
    dice = collections.Counter([DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 4


def test_seven_twos_rolled_six_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.TWO
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 6


def test_no_heals_rolled_no_heals_award():
    dice = collections.Counter([DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                DieValue.ENERGY, DieValue.ATTACK,
                                ])
    assert turn.calculate_heal_from_dice(dice) == 0


def test_three_attacks_rolled_three_attacks_award():
    dice = collections.Counter([DieValue.ONE, DieValue.ONE,
                                DieValue.HEAL, DieValue.ATTACK,
                                DieValue.ATTACK, DieValue.ATTACK,
                                ])
    assert turn.calculate_attack_from_dice(dice) == 3


def test_if_attackable_in_same_locations():
    player_one = Player()
    player_two = Player()
    assert not turn.if_attackable(player_one.location, player_two)


def test_if_attackable_in_different_locations():
    player_one = Player()
    player_two = Player()
    player_two.move_to_tokyo()
    assert turn.if_attackable(player_one.location, player_two)


def test_gets_all_attackable_players_in_different_location():
    attack_player = Player()
    player_two = Player()
    player_three = Player()
    player_four = Player()
    player_two.move_to_tokyo()
    player_four.move_to_tokyo()
    possible_players = [player_two, player_three, player_four]
    attackable_players = turn.get_attackable_players(
        attack_player, possible_players)
    assert attackable_players == [player_two, player_four]


def test_attacking_players_by_three():
    attack_player = Player()
    player_two = Player()
    player_three = Player()
    attackable_players = [player_two, player_three]
    turn.attack_players(attackable_players, -3)
    assert player_two.current_health == 7 and player_three.current_health == 7
