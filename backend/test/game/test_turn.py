import collections
import pytest

import backend.src.game.turn as turn
from backend.src.game.dice import DieValue


@pytest.fixture(autouse=True)
def dice_list():
    return collections.Counter([DieValue.TWO, DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.HEAL, DieValue.ATTACK,
                                DieValue.ENERGY])


def test_resolve_victory_points_dice(dice_list):
    assert turn.resolve_victory_points_dice(dice_list) == 3


def test_resolve_energy_dice(dice_list):
    assert turn.resolve_energy_dice(dice_list) == 1


def test_resolve_attack_dice(dice_list):
    assert turn.resolve_attack_dice(dice_list) == 1
