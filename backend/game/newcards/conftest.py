import pytest

from game.player import Player


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player
