import pytest

from backend.src.game.locations import Locations
from backend.src.game.player import Player


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


def test_player_default_health(player):
    assert player.default_health == 10


def test_player_default_location(player):
    assert player.location == Locations.OUTSIDE


def test_player_can_move_to_tokyo(player):
    player.move_to_tokyo()
    assert player.location == Locations.TOKYO


def test_player_can_leave_tokyo(player):
    player.leave_tokyo()
    assert player.location == Locations.OUTSIDE
