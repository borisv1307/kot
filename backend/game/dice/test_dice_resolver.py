import collections

from game.dice.dice import DieValue
import game.dice.dice_resolver as dice_resolver
from game.player.player import Player



def test_less_than_three_twos_rolled_no_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.HEAL, DieValue.ATTACK,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert dice_resolver.calculate_victory_points_from_dice(dice) == 0


def test_three_twos_rolled_two_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.HEAL,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert dice_resolver.calculate_victory_points_from_dice(dice) == 2


def test_four_twos_rolled_three_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert dice_resolver.calculate_victory_points_from_dice(dice) == 3


def test_five_threes_rolled_five_victory_points_awarded():
    dice = collections.Counter([DieValue.THREE, DieValue.THREE,
                                DieValue.THREE, DieValue.THREE,
                                DieValue.THREE, DieValue.ATTACK,
                                ])
    assert dice_resolver.calculate_victory_points_from_dice(dice) == 5


def test_six_ones_rolled_four_victory_points_awarded():
    dice = collections.Counter([DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                ])
    assert dice_resolver.calculate_victory_points_from_dice(dice) == 4


def test_seven_twos_rolled_six_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.TWO
                                ])
    assert dice_resolver.calculate_victory_points_from_dice(dice) == 6


def test_no_heals_rolled_no_heals_award():
    dice = collections.Counter([DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                DieValue.ENERGY, DieValue.ATTACK,
                                ])
    assert dice_resolver.calculate_heal_from_dice(dice) == 0


def test_three_attacks_rolled_three_attacks_award():
    dice = collections.Counter([DieValue.ONE, DieValue.ONE,
                                DieValue.HEAL, DieValue.ATTACK,
                                DieValue.ATTACK, DieValue.ATTACK,
                                ])
    assert dice_resolver.calculate_attack_from_dice(dice) == 3


def test_roll_energy_updates_player():
    player = Player()
    starting_energy = player.energy
    dice = [DieValue.ENERGY, DieValue.ENERGY,
            DieValue.ENERGY, DieValue.ENERGY,
            DieValue.ENERGY, DieValue.ENERGY]
    dice_resolver.dice_resolution(dice, player)
    assert player.energy == starting_energy + 6
