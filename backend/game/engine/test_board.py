import pickle

from game.engine.board import BoardGame
from game.player.player import Player
from game.values.constants import VICTORY_POINTS_TO_WIN
from game.values.status import Status


def test_before_game_starts():
    game = BoardGame()
    assert game.status == Status.SETUP


def test_after_game_starts():
    game = BoardGame()
    game.start_game()
    assert game.status == Status.ACTIVE


def test_game_stops():
    game = BoardGame()
    game.start_game()
    assert game.status != Status.COMPLETED
    game.end_game()
    assert game.status == Status.COMPLETED


def test_is_winner_by_points():
    game = BoardGame()
    player = Player()
    game.add_player(player)
    game.start_game()
    assert game.status == Status.ACTIVE
    current_player: Player = game.get_next_player_turn()
    current_player.update_victory_points_by(VICTORY_POINTS_TO_WIN)
    game.check_if_winner(current_player)
    assert game.status == Status.COMPLETED


def test_is_winner_by_death():
    game = BoardGame()
    game.add_player(Player())
    game.add_player(Player())
    game.start_game()
    assert game.status == Status.ACTIVE
    current_player: Player = game.get_next_player_turn()
    game.check_if_winner(current_player)
    assert game.status == Status.ACTIVE
    current_player.update_health_by(-current_player.current_health)
    current_player: Player = game.get_next_player_turn()
    game.check_if_winner(current_player)
    assert game.status == Status.COMPLETED


def test_get_next_player_turn_consistent_order():
    game = BoardGame()
    for _ in range(3):
        game.add_player(Player())
    game.start_game()
    player1 = game.get_next_player_turn()
    player2 = game.get_next_player_turn()
    player3 = game.get_next_player_turn()

    for _ in range(5):
        assert player1 is game.get_next_player_turn()
        assert player2 is game.get_next_player_turn()
        assert player3 is game.get_next_player_turn()


def test_board_pickling():
    game = BoardGame()
    serial_game = pickle.dumps(game)
    de_pickled_game: BoardGame = pickle.loads(serial_game)

