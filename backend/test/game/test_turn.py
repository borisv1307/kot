import collections
import pytest

import backend.src.game.turn as turn
from backend.src.game.dice import DieValue


@pytest.fixture(autouse=True)
def dice_list():
    return collections.Counter([DieValue.TWO, DieValue.TWO, DieValue.TWO,
                                DieValue.TWO, DieValue.HEAL, DieValue.ATTACK])


def test_resolve_victory_points_dice(dice_list):
    assert turn.resolve_victory_points_dice(dice_list) == 3
