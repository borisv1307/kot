import pytest

from game.player import Player
import game.turn_actions.player_movement as player_movement

@pytest.fixture(autouse=True)
def main_player():
    player_main = Player()
    return player_main


@pytest.fixture(autouse=True)
def other_players():
    player_a = Player()
    player_b = Player()
    player_c = Player()
    return [player_a, player_b, player_c]


def test_move_to_empty_tokyo(main_player, other_players):
    main_player.leave_tokyo()
    for player in other_players:
        player.leave_tokyo()
    player_movement.move_into_empty_tokyo(main_player, other_players)
    assert main_player.location == Locations