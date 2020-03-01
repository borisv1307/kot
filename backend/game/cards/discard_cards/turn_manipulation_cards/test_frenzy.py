from game.cards.discard_cards.turn_manipulation_cards.frenzy import Frenzy
from game.engine.board import BoardGame
from game.player.player import Player


def test_frenzy_grants_bonus_turn():
    board = BoardGame()
    board.add_player(Player("one"))
    board.add_player(Player("two"))
    board.start_game()
    current_player = board.players.get_current_player()
    current_player.energy = 100

    board.deck_handler.store[0] = Frenzy()
    board.deck_handler.buy_card_from_store(0, board.players.current_player,
                                           board.players.get_all_alive_players_minus_current_player())
    board.players.get_next_player()
    assert current_player.username == board.players.current_player.username
