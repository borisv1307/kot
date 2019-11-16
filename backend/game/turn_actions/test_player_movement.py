import pytest

from game.player.player import Player
import game.turn_actions.player_movement as player_movement
from game.values.locations import Locations
from game.dice.dice_resolver import dice_resolution
from game.dice.dice import DieValue
from game.values.constants import DEFAULT_HEALTH

MOCK_DICE_VALUES = [DieValue.ATTACK, DieValue.ATTACK, DieValue.HEAL, DieValue.HEAL, DieValue.HEAL, DieValue.HEAL]


@pytest.fixture(autouse=True)
def main_player():
    player_main = Player()
    player_main.location = Locations.OUTSIDE
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


def test_first_attack_roll_forces_move_to_tokyo(main_player, other_players):
    dice_resolution(MOCK_DICE_VALUES, main_player, other_players)
    assert main_player.location == Locations.TOKYO


def test_first_attack_roll_does_not_hurt_anyone(main_player, other_players):
    dice_resolution(MOCK_DICE_VALUES, main_player, other_players)
    assert all(others.current_health == DEFAULT_HEALTH for others in other_players)


def test_yield_on_death(main_player, other_players):
    player_a = other_players[0]
    player_a.location = Locations.TOKYO
    player_a.current_health = 1
    dice_resolution(MOCK_DICE_VALUES, main_player, other_players)
    assert main_player.location == Locations.TOKYO and not player_a.is_alive
