import pytest

from backend.src.game.engine import GameEngine
from backend.src.game.player import Player
from backend.src.game.status import Status


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


@pytest.fixture(autouse=True)
def game_engine():
    engine = GameEngine()
    return engine


def test_add_player(game_engine, player):
    game_engine.add_player(player)
    assert game_engine.players == [player]


def test_begin_game(game_engine):
    assert game_engine.players == game_engine.alive_players


def test_validate_if_winner(game_engine, player):
    player.change_victory_points(21)
    assert game_engine.validate_if_winner(player) == Status.GAME_OVER
