from game.engine.board import BoardGame
from game.player.player import Player
import game.values.status as status


def test_before_game_starts():
    game = BoardGame()
    assert game.status == status.SETUP


def test_after_game_starts():
    game = BoardGame()
    game.start_game()
    assert game.status == status.ACTIVE
