from typing import List

import pytest

import game.constants as constants
import game.test_constants as test_constants
from game.cards_old_dir.card import Card
from game.deck.deck_handler import DeckHandler


@pytest.fixture(autouse=True)
def deck_handler():
    deck_handler: DeckHandler = DeckHandler()
    return deck_handler


def test_deck_handler_init(deck_handler):
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == test_constants.JSON_CARD_COUNT - constants.CARD_STORE_SIZE_LIMITER


def test_buy_single_card(deck_handler):
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == test_constants.JSON_CARD_COUNT - constants.CARD_STORE_SIZE_LIMITER

    bought_card = deck_handler.buy_card_from_store(1)
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == test_constants.JSON_CARD_COUNT - constants.CARD_STORE_SIZE_LIMITER - 1
    assert not deck_handler.draw_pile.__contains__(bought_card)


def test_discard_card(deck_handler):
    assert len(deck_handler) == test_constants.JSON_CARD_COUNT
    card = deck_handler.buy_card_from_store(1)
    assert len(deck_handler) == test_constants.JSON_CARD_COUNT - 1
    deck_handler.discard(card)
    assert len(deck_handler) == test_constants.JSON_CARD_COUNT
    assert len(deck_handler.discard_pile) == 1


def test_force_shuffle_discard_add_to_draw(deck_handler):
    bought_cards: List[Card] = list()

    # buy 5 cards_old_dir
    for _ in range(5):
        bought_cards.append(deck_handler.buy_card_from_store(1))
    assert len(bought_cards) == 5
    assert len(deck_handler) == test_constants.JSON_CARD_COUNT - 5

    # discard the 5 cards_old_dir
    for card in bought_cards:
        deck_handler.discard(card)
    bought_cards.clear()
    assert len(deck_handler) == 66
    assert len(deck_handler.discard_pile) == 5

    # shuffle the 5 cards_old_dir and add to the draw pile
    deck_handler.shuffle_discard_pile_to_draw_pile()
    assert len(deck_handler) == 66
    assert len(deck_handler.discard_pile) == 0


def test_auto_reshuffle(deck_handler):
    bought_cards = list()

    # buy all cards_old_dir but 10
    for _ in range(test_constants.JSON_CARD_COUNT - 10):
        bought_cards.append(deck_handler.buy_card_from_store(1))
    assert len(deck_handler) == 10

    # move discard all bought cards_old_dir
    for card in bought_cards:
        deck_handler.discard(card)
    bought_cards.clear()
    assert len(deck_handler) == test_constants.JSON_CARD_COUNT
    assert len(deck_handler.draw_pile) == 7

    # buy all cards_old_dir but 10 again, forcing reshuffle discard to draw pile
    for _ in range(test_constants.JSON_CARD_COUNT - 10):
        bought_cards.append(deck_handler.buy_card_from_store(0))
    assert len(bought_cards) == test_constants.JSON_CARD_COUNT - 10
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler) == 10


def test_run_out_of_cards(deck_handler):
    # buy enough cards_old_dir to empty draw pile
    for _ in range(test_constants.JSON_CARD_COUNT - 3):
        (deck_handler.buy_card_from_store(0))
    assert len(deck_handler) == 3
    assert len(deck_handler.draw_pile) == 0

    # next card should raise an exception in deck_handler.fill_card_store
    with pytest.raises(Exception) as exception:
        assert deck_handler.buy_card_from_store(0)
    assert str(exception.value) == constants.OUT_OF_CARDS_MSG
