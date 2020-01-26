import pytest

from game.engine.player_queue import GamePlayers
from game.player.player import Player


def test_adding_player_to_queue():
    player = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player)
    assert player_queue.players == [player]


def test_adding_non_player_to_queue_raise_exception():
    player_queue = GamePlayers()
    with pytest.raises(TypeError):
        player_queue.add_player_to_game("NON_PLAYER")


def test_get_current_player_when_no_one_is_alive():
    player_queue = GamePlayers()
    with pytest.raises(Exception) as excinfo:
        player_queue.get_next_player()
    assert 'There are no alive players left' == str(excinfo.value)


def test_get_current_player_when_player_order_not_set():
    player = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player)
    assert player_queue.get_next_player() is None


def test_get_current_player_when_player_order_set():
    player1 = Player()
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    player_queue.set_player_order()
    player_queue.get_current_player()
    assert player_queue.current_player == player1


def test_get_next_player():
    player1 = Player()
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    player_queue.set_player_order()
    player_queue.get_next_player()
    player_queue.get_next_player()
    assert player_queue.current_player == player2


def test_get_alive_player():
    player1 = Player()
    player1.is_alive = False
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    assert player_queue.get_alive_players() == [player2]


def test_get_dead_player():
    player1 = Player()
    player1.is_alive = False
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    assert player_queue.get_dead_players() == [player1]


def test_get_all_alive_players_minus_current_player():
    player1 = Player()
    player1.is_alive = False
    player2 = Player()
    player3 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    player_queue.add_player_to_game(player3)
    player_queue.set_player_order()
    player_queue.get_current_player()
    assert player_queue.get_all_alive_players_minus_current_player() == [
        player3]


def test_when_last_player_is_alive():
    player1 = Player()
    player1.is_alive = False
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    assert player_queue.is_last_player_alive(player2) is True


def test_if_not_last_player_alive():
    player1 = Player()
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    assert player_queue.is_last_player_alive(player2) is False
