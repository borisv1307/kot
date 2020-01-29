import json
import re

import pytest
from mock import Mock

import game.dice.dice as dice
from game.dice.dice_handler import DiceHandler
from lobby.kot_object_serializer import KOTObjectSerializer

MOCK_SIX_DIE_VALUES_A = [dice.DieValue.ONE, dice.DieValue.TWO, dice.DieValue.THREE,
                         dice.DieValue.ATTACK, dice.DieValue.ENERGY, dice.DieValue.HEAL]

MOCK_SIX_VALUES_AFTER_RE_ROLL_DIE_ONE = [dice.DieValue.ATTACK, dice.DieValue.TWO, dice.DieValue.THREE,
                                         dice.DieValue.ATTACK, dice.DieValue.ENERGY, dice.DieValue.HEAL]

MOCK_DIE_ROLL_RESULT = dice.DieValue.ATTACK
MOCK_DIE_ROLL_RESULT_B = dice.DieValue.ENERGY

dice.roll = Mock(return_value=MOCK_DIE_ROLL_RESULT)
dice.roll_many = Mock(return_value=MOCK_SIX_DIE_VALUES_A)


@pytest.fixture(autouse=True)
def dice_handler():
    dice_handler = DiceHandler()
    dice_handler.roll_initial(6, 3)
    return dice_handler


def test_start_turn(dice_handler):
    for die in dice_handler.dice_values:
        assert die in dice.DieValue
    assert len(dice_handler.dice_values) == 6


def test_re_roll_one_die(dice_handler):
    dice_handler.re_roll_dice(0)
    assert dice_handler.dice_values == MOCK_SIX_VALUES_AFTER_RE_ROLL_DIE_ONE


def test_re_roll_all_dice(dice_handler):
    dice_handler.re_roll_dice([0, 1, 2, 3, 4, 5])
    for i in range(0, len(dice_handler.dice_values) - 1):
        assert dice_handler.dice_values[i] == MOCK_DIE_ROLL_RESULT


def test_re_roll_out_of_bounds_does_nothing(dice_handler):
    starting_dice_values = dice_handler.dice_values
    with pytest.raises(ValueError):
        dice_handler.re_roll_dice(9)
    assert dice_handler.dice_values == starting_dice_values


def test_re_roll_costs_re_roll_count(dice_handler):
    starting_re_roll_count = dice_handler.re_rolls_left
    dice_handler.re_roll_dice(2)
    assert dice_handler.re_rolls_left == starting_re_roll_count - 1


def test_re_roll_fail_does_not_cost_re_roll_count(dice_handler):
    starting_re_roll_count = dice_handler.re_rolls_left
    with pytest.raises(ValueError):
        dice_handler.re_roll_dice(20)
    assert dice_handler.re_rolls_left == starting_re_roll_count


def test_re_roll_bad_middle_index_cancels_re_roll(dice_handler):
    initial_vals = dice_handler.dice_values
    starting_re_roll_count = dice_handler.re_rolls_left
    with pytest.raises(ValueError):
        dice_handler.re_roll_dice([1, 30, 2])
    assert initial_vals == dice_handler.dice_values and dice_handler.re_rolls_left == starting_re_roll_count


def test_bad_value_throws_exception(dice_handler):
    with pytest.raises(ValueError):
        assert dice_handler.re_roll_dice(99)


def test_add_one_bonus_die(dice_handler):
    start_die_count = len(dice_handler.dice_values)
    dice_handler.add_bonus_die()
    assert len(dice_handler.dice_values) == start_die_count + 1
    last_die_index = len(dice_handler.dice_values) - 1
    assert dice_handler.dice_values[last_die_index] == MOCK_DIE_ROLL_RESULT


def test_add_3_bonus_dice(dice_handler):
    start_die_count = len(dice_handler.dice_values)
    dice_handler.add_bonus_die(3)
    assert len(dice_handler.dice_values) == start_die_count + 3
    last_die_index = len(dice_handler.dice_values) - 1
    assert dice_handler.dice_values[last_die_index] == MOCK_DIE_ROLL_RESULT


def test_roll_bonus_die(dice_handler):
    dice_handler.add_bonus_die()
    last_die_index = len(dice_handler.dice_values) - 1
    bonus_die_initial_val = dice_handler.dice_values[last_die_index]
    assert bonus_die_initial_val == MOCK_DIE_ROLL_RESULT

    dice.roll = Mock(return_value=MOCK_DIE_ROLL_RESULT_B)
    dice_handler.re_roll_dice([last_die_index])
    assert dice_handler.dice_values[last_die_index] == MOCK_DIE_ROLL_RESULT_B


def test_serialize():
    dh = DiceHandler()
    dh.roll_initial(6, 3)
    print("\n\n")
    print("re rolls left = {}".format(dh.re_rolls_left))
    encoded_dh = json.dumps(dh.serialize_kot_obj(), cls=KOTObjectSerializer)
    print("the json data is:\n{}".format(encoded_dh))
    assert re.match(".*dice_handler.*dice_values.*(die_val.*){6}re_rolls_left.*", encoded_dh, )
