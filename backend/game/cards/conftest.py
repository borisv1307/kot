import pytest

from game.player.player import Player


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


@pytest.fixture(autouse=True)
def five_players():
    players = [Player() for i in range(5)]
    return players
