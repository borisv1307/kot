import pytest
import game.values.constants as constants
import game.turn_actions.heal as heal
from game.player.player import Player


@pytest.fixture(autouse=True)
def player():
    player: Player = Player()
    return player


def test_heal_only_in_tokyo(player):
    player.leave_tokyo()
    starting_health = player.current_health
    player.update_health_by(-3)
    heal.heal_self(player, 1)
    assert player.current_health == starting_health - 2

    player.move_to_tokyo()
    heal.heal_self(player, 1)
    assert player.current_health == starting_health - 2