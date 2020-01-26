from game.engine.board import BoardGame
from game.player.player import Player
from game.values.status import Status


def test_before_game_starts():
    game = BoardGame()
    assert game.status == Status.SETUP


def test_after_game_starts():
    game = BoardGame()
    game.start_game()
    assert game.status == Status.ACTIVE
