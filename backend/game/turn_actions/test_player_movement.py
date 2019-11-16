import pytest

from game.player.player import Player
import game.turn_actions.player_movement as player_movement
from game.values.locations import Locations


@pytest.fixture(autouse=True)
def main_player():
    player_main = Player()
    return player_main


@pytest.fixture(autouse=True)
def other_players():
    player_a = Player()
    player_b = Player()
    player_c = Player()
    players = [player_a, player_b, player_c]
    for player in players:
        player.location = Locations.OUTSIDE
    return players


def test_move_to_empty_tokyo(main_player, other_players):
    player_movement.move_to_tokyo_if_empty(main_player, other_players)
    assert main_player.location == Locations.TOKYO


def test_stay_out_occupied_tokyo(main_player, other_players):
    other_players[0].location = Locations.TOKYO
    player_movement.move_to_tokyo_if_empty(main_player, other_players)
    assert main_player.location == Locations.OUTSIDE


def test_yield_tokyo(main_player, other_players):
    main_player.location = Locations.TOKYO
    player_a = other_players[0]
    player_movement.yield_tokyo(main_player, player_a)
    assert main_player.location == Locations.OUTSIDE and player_a.location == Locations.TOKYO
