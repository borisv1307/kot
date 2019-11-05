import pytest
from backend.src.game.dice_handler import DiceHandler
import backend.src.game.dice.dice as dice
from mock import Mock

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
    dice_handler.start_turn(6, 3)
    return dice_handler


def test_start_turn(dice_handler):
    for die in dice_handler.dice_values:
        assert die in dice.DieValue
    assert len(dice_handler.dice_values) == 6


def test_re_roll_one_die(dice_handler):
    dice_handler.re_roll_dice([0])
    assert dice_handler.dice_values == MOCK_SIX_VALUES_AFTER_RE_ROLL_DIE_ONE


def test_re_roll_all_dice(dice_handler):
    dice_handler.re_roll_dice([0, 1, 2, 3, 4, 5])
    for i in range(0, len(dice_handler.dice_values)-1):
        assert dice_handler.dice_values[i] == MOCK_DIE_ROLL_RESULT


def test_re_roll_out_of_bounds_throws_exception(dice_handler):
    with pytest.raises(IndexError):
        assert dice_handler.re_roll_dice([9])


def test_incorrect_type_passed_re_roll_throws_exception(dice_handler):
    with pytest.raises(TypeError):
        assert dice_handler.re_roll_dice(["BAD VALUE"])


def test_add_die(dice_handler):
    start_die_count = len(dice_handler.dice_values)
    dice_handler.add_bonus_die()
    assert len(dice_handler.dice_values) == start_die_count + 1
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
