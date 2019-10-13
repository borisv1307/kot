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


def test_begin_game(game_engine, player):
    game_engine.add_player(player)
    game_engine.begin_game()
    assert game_engine.players == game_engine.alive_players
    assert game_engine.game_status == Status.ACTIVE


def test_validate_if_player_wins(game_engine, player):
    player.change_victory_points(21)
    game_engine.validate_if_winner(player)
    assert game_engine.game_status == Status.GAME_OVER


def test_check_alive_dead_players(game_engine, player):
    player_1 = player
    player_1.change_health(-11)
    player_2 = player
    game_engine.add_player(player_1)
    game_engine.add_player(player_2)
    game_engine.begin_game()
    game_engine.set_dead_players()
    assert game_engine.dead_players == [player_1]
    assert game_engine.alive_players == [player_2]
