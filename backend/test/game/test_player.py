import pytest

from backend.src.game import constants
from backend.src.game.locations import Locations
from backend.src.game.player import Player


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


def test_player_default_health(player):
    assert player.maximum_health == constants.DEFAULT_HEALTH


def test_player_default_location(player):
    assert player.location == Locations.OUTSIDE


def test_player_can_move_to_tokyo(player):
    player.move_to_tokyo()
    assert player.location == Locations.TOKYO


def test_player_can_leave_tokyo(player):
    player.leave_tokyo()
    assert player.location == Locations.OUTSIDE


def test_player_current_health_is_maximum_health_when_created(player):
    assert player.current_health == player.maximum_health


def test_player_got_hurt_by_one(player):
    player.change_health(-1)
    assert player.current_health == player.maximum_health - 1


def test_player_got_hurt_by_three_and_healed_by_1(player):
    player.change_health(-3)
    player.change_health(1)
    assert player.current_health == player.maximum_health - 2


def test_player_health_can_not_exceed_max_health(player):
    player.change_health(1)
    assert player.current_health == player.maximum_health


def test_player_dies_when_current_health_hits_zero(player):
    player.change_health(-10)
    assert not player.is_alive


def test_player_starts_with_zero_victory_points(player):
    assert player.victory_points == constants.ZERO


def test_player_can_gain_victory_points(player):
    player.change_victory_points(10)
    assert player.victory_points == 10


def test_player_can_lose_victory_points(player):
    player.change_victory_points(10)
    player.change_victory_points(-5)
    assert player.victory_points == 5


def test_player_can_not_have_less_than_zero_victory_points(player):
    player.change_victory_points(-1)
    assert player.victory_points == 0
