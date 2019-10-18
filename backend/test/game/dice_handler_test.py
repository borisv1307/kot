import pytest
from backend.src.game.dice_handler import DiceHandler
import backend.src.game.dice as dice


@pytest.fixture(autouse=True)
def dice_handler():
    dice_handler = DiceHandler()
    return dice_handler


def test_start_turn(dice_handler):
    for die in dice_handler.dice_values:
        assert die in dice.DieValue


def test_re_roll_one_die(dice_handler):
    dice_handler.start_turn()
    start_value = dice_handler.dice_values[0]
    roll_changed_value = False
    # since technically possible re-roll returns same roll, run 10 times and quit on successful result
    for _ in range(10):
        dice_handler.re_roll_dice(0)
        if not start_value == dice_handler.dice_values[0]:
            roll_changed_value = True
            break
    assert roll_changed_value


def test_re_roll_all_dice(dice_handler):
    dice_handler.start_turn()
    start_values = dice_handler.dice_values.copy()
    dice_handler.re_roll_dice([0, 1, 2, 3, 4, 5])
    all_elements_are_same = True
    for i in range(0, len(dice_handler.dice_values)-1):
        if not start_values[i] == dice_handler.dice_values[i]:
            all_elements_are_same = False
            break
    assert not all_elements_are_same


def test_add_die(dice_handler):
    dice_handler.start_turn()

    # assert there's another die
    start_die_count = len(dice_handler.dice_values)
    dice_handler.add_bonus_die()
    assert len(dice_handler.dice_values) > start_die_count

    # assert the last die can be rerolled
    last_die_index = len(dice_handler.dice_values) - 1
    bonus_die_initial_val = dice_handler.dice_values[last_die_index]
    bonus_die_changed = False
    # since technically possible re-roll returns same roll, run 10 times and quit on successful result
    for i in range(10):
        dice_handler.re_roll_dice(last_die_index)
        if not dice_handler.dice_values[last_die_index] == bonus_die_initial_val:
            bonus_die_changed = True
            break
    assert bonus_die_changed
