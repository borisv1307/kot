import json

from game.engine.player_queue import GamePlayers
from game.player.player import Player
from game.player.player_status_resolver import generate_player_status_summary, player_status_summary_to_JSON


def test_generate_player_status_summary():
    player1 = Player()
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    player_queue.set_player_order()
    actual_summary: [] = generate_player_status_summary(player_queue)
    expected_p1_dictionary = player1.generate_player_status_as_dictionary()
    expected_p2_dictionary = player2.generate_player_status_as_dictionary()
    expected_summary: [] = [expected_p1_dictionary, expected_p2_dictionary]
    print(expected_summary)
    print(actual_summary)
    assert actual_summary == expected_summary


def test_player_status_summary_to_JSON():
    player1 = Player()
    player2 = Player()
    player_queue = GamePlayers()
    player_queue.add_player_to_game(player1)
    player_queue.add_player_to_game(player2)
    player_queue.set_player_order()
    actual_summary_json = player_status_summary_to_JSON(player_queue)
    expected_p1_dictionary = player1.generate_player_status_as_dictionary()
    expected_p2_dictionary = player2.generate_player_status_as_dictionary()
    expected_summary_json: [] = json.dumps([expected_p1_dictionary, expected_p2_dictionary])
    assert actual_summary_json == expected_summary_json
