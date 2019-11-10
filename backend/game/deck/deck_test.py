import pytest

import game.definitions.test_constants as constants
from game.deck.deck import Deck


@pytest.fixture(autouse=True)
def deck():
    deck = Deck()
    return deck


def test_deck_init(deck):
    assert len(deck) == 0
    deck.get_new_deck()
    assert len(deck) == constants.JSON_CARD_COUNT


def test_draw_card(deck):
    deck.get_new_deck()
    original_deck_size = len(deck)
    card = deck.draw_from()
    assert not deck.__contains__(card)
    assert len(deck) == original_deck_size - 1
