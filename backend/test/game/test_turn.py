import collections
import pytest

import backend.src.game.turn as turn
from backend.src.game.dice.dice import DieValue


def test_less_than_three_victory_point_dice_no_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.HEAL, DieValue.ATTACK,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 0


def test_three_victory_point_dice_two_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.HEAL,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 2


def test_four_victory_point_dice_three_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.HEAL, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 3


def test_five_victory_point_dice_five_victory_points_awarded():
    dice = collections.Counter([DieValue.THREE, DieValue.THREE,
                                DieValue.THREE, DieValue.THREE,
                                DieValue.THREE, DieValue.ATTACK,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 5


def test_six_victory_point_dice_four_victory_points_awarded():
    dice = collections.Counter([DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                DieValue.ONE, DieValue.ONE,
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 4


def test_seven_victory_point_dice_six_victory_points_awarded():
    dice = collections.Counter([DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.TWO,
                                DieValue.TWO
                                ])
    assert turn.calculate_victory_points_from_dice(dice) == 6
