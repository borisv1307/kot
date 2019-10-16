import pytest

import backend.src.game.dice as dice


def test_roll():
    assert dice.roll() in dice.DieValue
