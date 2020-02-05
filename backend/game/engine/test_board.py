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
    game.add_player(Player("Awesome_player_1"))
    game.add_player(Player("Please don't pickle me"))
    game.start_game()
    player_whos_turn_it_is = game.players.get_current_player()
    assert game.is_game_active()

    serial_game = pickle.dumps(game)
    de_pickled_game: BoardGame = pickle.loads(serial_game)
    players = de_pickled_game.players
    assert player_whos_turn_it_is == de_pickled_game.players.get_current_player()

    assert de_pickled_game.is_game_active()
    assert len(players.players) == 2


def test_full_turns():
    # Scratch pad to step through turn actions for testing
    player1 = Player("I AM NUMBER UNO!")
    player2 = Player("PLAYEER ONE SUX")
    game = BoardGame()
    game.add_player(player1)
    game.add_player(player2)
    game.start_game()

    print("\n\nDEBUG OUTPUT:\n")
    print("CURRENT PLAYER:" + game.players.get_current_player().username)

    dice_count_for_test = 6
    reroll_count_for_test = 2
    dice_to_reroll_in_test = [0, 1, 2]

    game.dice_handler.roll_initial(dice_count_for_test, reroll_count_for_test)

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice(dice_to_reroll_in_test)

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice(dice_to_reroll_in_test)

    print(game.dice_handler.dice_values)
    try:
        game.dice_handler.re_roll_dice(dice_to_reroll_in_test)
    except ValueError:
        print("attempted too many re-rolls, refusing to re-roll")
    returned_Player = game.get_next_player_turn()

    print("CURRENT PLAYER = " + returned_Player.username)

    game.dice_handler.roll_initial(dice_count_for_test, reroll_count_for_test)

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice(dice_to_reroll_in_test)

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice(dice_to_reroll_in_test)

    print(game.dice_handler.dice_values)
    try:
        game.dice_handler.re_roll_dice(dice_to_reroll_in_test)
    except ValueError:
        print("attempted too many re-rolls, refusing to re-roll")
    returned_player = game.get_next_player_turn()
    print("CURRENT PLAYER = " + returned_player.username)
