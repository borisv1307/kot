import pytest
import game.turn_actions.heal as heal
from game.player.player import Player
from game.values.locations import Locations
from game.dice.dice import DieValue
from game.dice.dice_resolver import dice_resolution

MOCK_DICE_RESULTS = [DieValue.HEAL, DieValue.HEAL, DieValue.HEAL, DieValue.ATTACK, DieValue.ATTACK, DieValue.ATTACK]


@pytest.fixture(autouse=True)
def hurt_player():
    hurt_player: Player = Player()
    hurt_player.update_health_by(-3)
    return hurt_player


def test_heal_from_dice_out_of_tokyo(hurt_player):
    hurt_player.location = Locations.OUTSIDE
    starting_health = hurt_player.current_health
    heal.heal_self_from_dice(hurt_player, 1)
    assert hurt_player.current_health == starting_health + 1


def test_no_heal_from_dice_in_tokyo(hurt_player):
    hurt_player.move_to_tokyo()
    starting_health = hurt_player.current_health
    heal.heal_self_from_dice(hurt_player, 1)
    assert hurt_player.current_health == starting_health


def test_resolve_dice_and_heal(hurt_player):
    initial_health = hurt_player.current_health
    dice_resolution(MOCK_DICE_RESULTS, hurt_player)
    assert hurt_player.current_health == initial_health + MOCK_DICE_RESULTS.count(DieValue.HEAL)
