import pytest

from backend.src.game.player import Player


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player
