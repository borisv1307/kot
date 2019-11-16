import pytest
import game.turn_actions.heal as heal
from game.player.player import Player


@pytest.fixture(autouse=True)
def hurt_player():
    hurt_player: Player = Player()
    hurt_player.update_health_by(-3)
    return hurt_player


def test_heal_from_dice_out_of_tokyo(hurt_player):
    hurt_player.leave_tokyo()
    starting_health = hurt_player.current_health
    heal.heal_self_from_dice(hurt_player, 1)
    assert hurt_player.current_health == starting_health + 1


def test_no_heal_from_dice_in_tokyo(hurt_player):
    hurt_player.move_to_tokyo()
    starting_health = hurt_player.current_health
    heal.heal_self_from_dice(hurt_player, 1)
    assert hurt_player.current_health == starting_health
