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
    game.add_player(Player())
    game.start_game()
    assert game.status == Status.ACTIVE


def test_game_stops():
    game = BoardGame()
    game.add_player(Player())
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
    player1 = Player("I AM NUMBER UNO!")
    player2 = Player("PLAYEER ONE SUX")
    game = BoardGame()
    game.add_player(player1)
    game.add_player(player2)
    game.start_game()

    for _ in range(10):
        print("CURRENT PLAYER:" + game.get_next_player_turn().username)

    game.dice_handler.roll_initial(6, 2)

    num_players = len(game.players.get_alive_players())

    print("\n\nDEBUG OUTPUT:\n")
    print("CURRENT PLAYER:" + game.players.get_current_player().username)

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice([1, 2, 3])

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice([1, 2, 3])

    print(game.dice_handler.dice_values)
    try:
        game.dice_handler.re_roll_dice([1, 2, 3])
    except ValueError:
        print("failed too many rerolls")
    returned_Player = game.get_next_player_turn()

    print("CURRENT PLAYER = " + returned_Player.username)

    game.dice_handler.roll_initial(6, 2)

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice([1, 2, 3])

    print(game.dice_handler.dice_values)
    game.dice_handler.re_roll_dice([1, 2, 3])

    print(game.dice_handler.dice_values)
    try:
        game.dice_handler.re_roll_dice([1, 2, 3])
    except ValueError:
        print("failed too many rerolls")
    returned_Player = game.get_next_player_turn()
    print("CURRENT PLAYER = " + returned_Player.username)


def test_decode_selected_dice_indexes():
    payload = [['e', True], ['1', False], ['h', True], ['2', False], ['3', True], ['e', False]]
    i = 0
    indexes = []
    for item in payload:
        if item[1] == True:
            indexes.append(i)
        i += 1
    assert indexes == [0, 2, 4]
