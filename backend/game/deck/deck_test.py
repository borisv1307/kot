import pytest

from game.deck.deck import Deck
import game.cards.master_card_list as master_card_list

NUMBER_OF_CARDS_IN_GAME = master_card_list.get_all_cards().__len__()


@pytest.fixture(autouse=True)
def deck():
    deck = Deck()
    return deck


def test_deck_init(deck):
    assert len(deck) == 0
    deck.get_new_deck()
    assert len(deck) == NUMBER_OF_CARDS_IN_GAME
    print(len(deck))


def test_draw_card(deck):
    deck.get_new_deck()
    original_deck_size = len(deck)
    card = deck.draw_from()
    assert not deck.__contains__(card)
    assert len(deck) == original_deck_size - 1
