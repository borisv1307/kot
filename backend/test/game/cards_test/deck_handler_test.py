from typing import List

import pytest

import backend.src.game.cards.definitions as definitions
from backend.src.game.cards.card import Card
from backend.src.game.cards.deck_handler import DeckHandler


@pytest.fixture(autouse=True)
def deck_handler():
    deck_handler: DeckHandler = DeckHandler()
    return deck_handler


def test_deck_handler_init(deck_handler):
    print(len(deck_handler.store))
    print(len(deck_handler.draw_pile))
    assert len(deck_handler.store) == definitions.CARD_STORE_SIZE
    assert len(deck_handler.draw_pile) == definitions.JSON_CARD_COUNT - definitions.CARD_STORE_SIZE


def test_buy_single_card(deck_handler):
    assert len(deck_handler.store) == definitions.CARD_STORE_SIZE
    assert len(deck_handler.draw_pile) == definitions.JSON_CARD_COUNT - definitions.CARD_STORE_SIZE

    bought_card = deck_handler.buy_card(1)
    assert len(deck_handler.store) == definitions.CARD_STORE_SIZE
    assert len(deck_handler.draw_pile) == definitions.JSON_CARD_COUNT - definitions.CARD_STORE_SIZE - 1
    assert not deck_handler.draw_pile.__contains__(bought_card)


def test_discard_card(deck_handler):
    assert len(deck_handler) == definitions.JSON_CARD_COUNT
    card = deck_handler.buy_card(1)
    assert len(deck_handler) == definitions.JSON_CARD_COUNT - 1
    deck_handler.discard(card)
    assert len(deck_handler) == definitions.JSON_CARD_COUNT
    assert len(deck_handler.discard_pile) == 1


def test_force_shuffle_discard_add_to_draw(deck_handler):
    bought_cards: List[Card] = list()

    # buy 5 cards
    for _ in range(5):
        bought_cards.append(deck_handler.buy_card(1))
    assert len(bought_cards) == 5
    assert len(deck_handler) == definitions.JSON_CARD_COUNT - 5

    # discard the 5 cards
    for card in bought_cards:
        deck_handler.discard(card)
    bought_cards.clear()
    assert len(deck_handler) == 66
    assert len(deck_handler.discard_pile) == 5

    # shuffle the 5 cards and add to the draw pile
    deck_handler.shuffle_discard_pile_to_draw_pile()
    assert len(deck_handler) == 66
    assert len(deck_handler.discard_pile) == 0


def test_auto_reshuffle(deck_handler):
    bought_cards = list()

    # buy all cards but 10
    for _ in range(definitions.JSON_CARD_COUNT - 10):
        bought_cards.append(deck_handler.buy_card(1))
    assert len(deck_handler) == 10

    # move discard all bought cards
    for card in bought_cards:
        deck_handler.discard(card)
    bought_cards.clear()
    assert len(deck_handler) == definitions.JSON_CARD_COUNT
    assert len(deck_handler.draw_pile) == 7

    # buy all cards but 10 again, forcing reshuffle discard to draw pile
    for _ in range(definitions.JSON_CARD_COUNT - 10):
        bought_cards.append(deck_handler.buy_card(0))
    assert len(bought_cards) == definitions.JSON_CARD_COUNT - 10
    assert len(deck_handler.store) == definitions.CARD_STORE_SIZE
    assert len(deck_handler) == 10


def test_run_out_of_cards(deck_handler):
    # buy enough cards to empty draw pile
    for _ in range(definitions.JSON_CARD_COUNT - 3):
        (deck_handler.buy_card(0))
    assert len(deck_handler) == 3
    assert len(deck_handler.draw_pile) == 0

    # next card should raise an exception in deck_handler.fill_card_store
    with pytest.raises(Exception) as exception:
        assert deck_handler.buy_card(0)
    assert str(exception.value) == definitions.OUT_OF_CARDS_MSG
