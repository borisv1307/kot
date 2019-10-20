import collections
import pytest

import backend.src.game.turn as turn
from backend.src.game.dice import DieValue


def test_calculate_victory_points_from_dice():
    two_dice_list = collections.Counter([DieValue.TWO, DieValue.TWO,
                                         DieValue.HEAL, DieValue.ATTACK])
    three_dice_list = collections.Counter([DieValue.TWO, DieValue.TWO,
                                           DieValue.TWO, DieValue.HEAL,
                                           DieValue.ATTACK])
    four_dice_list = collections.Counter([DieValue.TWO, DieValue.TWO,
                                          DieValue.TWO, DieValue.TWO,
                                          DieValue.HEAL, DieValue.HEAL,
                                          DieValue.ENERGY])
    five_dice_list = collections.Counter([DieValue.THREE, DieValue.THREE,
                                          DieValue.THREE, DieValue.THREE,
                                          DieValue.THREE, DieValue.ATTACK,
                                          DieValue.ENERGY])
    six_dice_list = collections.Counter([DieValue.ONE, DieValue.ONE,
                                         DieValue.ONE, DieValue.ONE,
                                         DieValue.ONE, DieValue.ONE
                                         ])
    assert turn.calculate_victory_points_from_dice(two_dice_list) == 0
    assert turn.calculate_victory_points_from_dice(three_dice_list) == 2
    assert turn.calculate_victory_points_from_dice(four_dice_list) == 3
    assert turn.calculate_victory_points_from_dice(five_dice_list) == 5
    assert turn.calculate_victory_points_from_dice(six_dice_list) == 6
