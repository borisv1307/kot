from game.cards.keep_cards.turn_manipulation_cards.GiantBrain import GiantBrain
from game.engine.board import BoardGame
from game.player.player import Player
from game.values import constants


def test_giant_brain_grants_bonus_die():
    board = BoardGame()
    board.add_player(Player("one"))
    board.add_player(Player("two"))
    board.start_game()
    current_player = board.players.get_current_player()
    current_player.energy = 100

    board.deck_handler.store[0] = GiantBrain()
    board.deck_handler.buy_card_from_store(0, board.players.current_player,
                                           board.players.get_all_alive_players_minus_current_player())

    board.dice_handler.roll_initial(board.players.current_player.dice_allowed, 2)
    assert len(board.dice_handler.dice_values) == constants.DEFAULT_DICE_TO_ROLL + 1
    board.players.get_next_player()
    board.dice_handler.roll_initial(board.players.current_player.dice_allowed, 2)
    assert len(board.dice_handler.dice_values) == constants.DEFAULT_DICE_TO_ROLL
