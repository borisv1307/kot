from typing import List

import pytest

import game.values.constants as constants
import game.values.test_constants as test_constants
from game.cards.card import Card
from game.deck.deck_handler import DeckHandler

import game.cards.master_card_list as master_card_list

NUMBER_OF_CARDS_IN_GAME = master_card_list.get_all_cards().__len__()

@pytest.fixture(autouse=True)
def deck_handler():
    deck_handler: DeckHandler = DeckHandler()
    return deck_handler


def test_deck_handler_init(deck_handler):
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER


def test_buy_single_card(deck_handler):
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER

    bought_card = deck_handler.buy_card_from_store(1)
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER - 1
    assert not deck_handler.draw_pile.__contains__(bought_card)


def test_discard_card(deck_handler):
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    card = deck_handler.buy_card_from_store(1)
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME - 1
    deck_handler.discard(card)
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    assert len(deck_handler.discard_pile) == 1


def test_force_shuffle_discard_add_to_draw(deck_handler):
    bought_cards: List[Card] = list()

    # buy all cards but the 3 in the store
    for _ in range(NUMBER_OF_CARDS_IN_GAME - 3):
        bought_cards.append(deck_handler.buy_card_from_store(1))
    assert len(bought_cards) == NUMBER_OF_CARDS_IN_GAME - 3


    # discard the 5 cards_old_dir
    for card in bought_cards:
        deck_handler.discard(card)
    bought_cards.clear()
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    assert len(deck_handler.discard_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER

    # shuffle the discarded cards and add to the draw pile
    deck_handler.shuffle_discard_pile_to_draw_pile()
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    assert len(deck_handler.discard_pile) == 0


def test_auto_reshuffle(deck_handler):
    bought_cards = list()

    # buy all cards but 1 and the store
    for _ in range(NUMBER_OF_CARDS_IN_GAME - (1 + constants.CARD_STORE_SIZE_LIMITER)):
        bought_cards.append(deck_handler.buy_card_from_store(1))
    assert len(deck_handler) == 1 + constants.CARD_STORE_SIZE_LIMITER

    # move discard all bought cards
    for card in bought_cards:
        deck_handler.discard(card)
    bought_cards.clear()
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    assert len(deck_handler.draw_pile) == 1



    # buy all card but 1 and the store again, forcing reshuffle discard to draw pile
    for _ in range(NUMBER_OF_CARDS_IN_GAME - (1 + constants.CARD_STORE_SIZE_LIMITER)):
        bought_cards.append(deck_handler.buy_card_from_store(0))
    assert len(bought_cards) == NUMBER_OF_CARDS_IN_GAME - (1 + constants.CARD_STORE_SIZE_LIMITER)
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler) == 1 + constants.CARD_STORE_SIZE_LIMITER


def test_run_out_of_cards(deck_handler):
    # buy enough cards_old_dir to empty draw pile
    for _ in range(NUMBER_OF_CARDS_IN_GAME - 3):
        (deck_handler.buy_card_from_store(0))
    assert len(deck_handler) == 3
    assert len(deck_handler.draw_pile) == 0

    # next card should raise an exception in deck_handler.fill_card_store
    with pytest.raises(Exception) as exception:
        assert deck_handler.buy_card_from_store(0)
    assert str(exception.value) == constants.OUT_OF_CARDS_MSG
