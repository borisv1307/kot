from typing import List

import pytest

import game.cards.master_card_list as master_card_list
import game.values.constants as constants
from game.cards.card import Card
from game.cards.keep_card import KeepCard
from game.deck.deck_handler import DeckHandler
from game.player.player import Player

NUMBER_OF_CARDS_IN_GAME = len(master_card_list.get_all_cards())


@pytest.fixture(autouse=True)
def deck_handler():
    deck_handler: DeckHandler = DeckHandler()
    return deck_handler


@pytest.fixture(autouse=True)
def rich_player():
    rich_player: Player = Player()
    rich_player.energy = 100
    return rich_player


def test_deck_handler_init(deck_handler):
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER


def test_buy_single_card(deck_handler, rich_player):
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER

    bought_card = deck_handler.buy_card_from_store(1, rich_player)
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER - 1
    assert not deck_handler.draw_pile.__contains__(bought_card)
    while True:
        rich_player.update_energy_by(100)
        card_to_purchase = deck_handler.store[0]
        deck_handler.buy_card_from_store(0, rich_player)
        if isinstance(card_to_purchase, KeepCard):
            assert rich_player.has_instance_of_card(card_to_purchase)
            break


def test_discard_card(deck_handler, rich_player):
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    while True:
        card_player_will_buy = deck_handler.store[0]
        deck_handler.buy_card_from_store(0, rich_player)
        if isinstance(card_player_will_buy, KeepCard):
            # exit after buying one keep card
            break
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME - 1
    assert rich_player.cards.__contains__(card_player_will_buy)
    deck_handler.discard(card_player_will_buy, rich_player.cards)
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    assert len(rich_player.cards) == 0


def test_cards_cost_energy(deck_handler, rich_player):
    initial_energy = rich_player.energy
    card_player_will_buy = deck_handler.store[1]
    deck_handler.buy_card_from_store(1, rich_player)
    assert rich_player.energy == initial_energy - card_player_will_buy.cost


def test_cards_bought_are_added_to_player(deck_handler, rich_player):
    while True:
        card_player_will_buy = deck_handler.store[0]
        deck_handler.buy_card_from_store(0, rich_player)
        if isinstance(card_player_will_buy, KeepCard):
            assert rich_player.has_instance_of_card(card_player_will_buy)
            break


def test_force_shuffle_discard_add_to_draw(deck_handler, rich_player):
    bought_cards: List[Card] = list()

    # buy all cards but the 3 in the store, reset energy to never run out for test
    for _ in range(NUMBER_OF_CARDS_IN_GAME - 3):
        rich_player.energy = 100
        deck_handler.buy_card_from_store(1, rich_player)

    assert len(deck_handler.draw_pile) == 0

    deck_handler.buy_card_from_store(0, rich_player)

    assert len(deck_handler.draw_pile) > 0


def test_auto_reshuffle(deck_handler, rich_player):
    # buy all cards but 1 and the store
    for _ in range(NUMBER_OF_CARDS_IN_GAME - (1 + constants.CARD_STORE_SIZE_LIMITER)):
        rich_player.energy = 100
        deck_handler.buy_card_from_store(1, rich_player)
    #  Now there's only one in the draw pile, and the three in the store
    assert len(deck_handler.draw_pile) == 1

    # buy all card but 1 and the store again, forcing reshuffle discard to draw pile, reset energy to never run out
    for _ in range(NUMBER_OF_CARDS_IN_GAME - (1 + constants.CARD_STORE_SIZE_LIMITER)):
        rich_player.energy = 100
        deck_handler.buy_card_from_store(0, rich_player)


def test_do_not_sell_card_to_player_with_no_energy(deck_handler):
    poor_player = Player()
    poor_player.energy = 0
    with pytest.raises(Exception) as raised_exception:
        deck_handler.buy_card_from_store(1, poor_player)
    assert constants.INSUFFICIENT_FUNDS_MSG in str(raised_exception.value)


def test_sweep_store_not_allowed_with_insufficient_energy(deck_handler):
    test_player = Player()
    test_player.energy = 0
    with pytest.raises(Exception) as exception:
        deck_handler.sweep_store(test_player)
    assert str(exception.value) == constants.INSUFFICIENT_FUNDS_TO_SWEEP_MSG


def test_sweep_store_takes_current_cards_from_store(deck_handler):
    test_player = Player()
    test_player.energy = constants.SWEEP_CARD_STORE_COST
    initial_cards_in_store = [deck_handler.store[0], deck_handler.store[1], deck_handler.store[2]]
    deck_handler.sweep_store(test_player)
    for card in initial_cards_in_store:
        assert not deck_handler.store.__contains__(card)


def test_sweep_store_puts_current_cards_in_discard(deck_handler):
    test_player = Player()
    test_player.energy = constants.SWEEP_CARD_STORE_COST
    initial_cards_in_store = [deck_handler.store[0], deck_handler.store[1], deck_handler.store[2]]
    deck_handler.sweep_store(test_player)
    for card in initial_cards_in_store:
        assert deck_handler.discard_pile.__contains__(card)


def test_sweep_store_costs_energy(deck_handler):
    test_player = Player()
    test_player.energy = constants.SWEEP_CARD_STORE_COST
    deck_handler.sweep_store(test_player)
    assert test_player.energy == 0


def test_store_refills_after_sweep(deck_handler):
    test_sweep_store_costs_energy(deck_handler)
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
