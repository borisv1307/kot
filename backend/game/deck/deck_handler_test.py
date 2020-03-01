import itertools
from typing import List

import pytest

import game.values.constants as constants
from game.cards.card import Card
from game.cards.discard_cards.health_manipulation_cards.heal import Heal
from game.cards.keep_cards.health_manipulation_cards.even_bigger import EvenBigger
from game.deck.deck_handler import DeckHandler
from game.player.player import Player

NUMBER_OF_CARDS_IN_GAME = 10
SAMPLE_KEEP_CARD = EvenBigger()
SAMPLE_DISCARD_CARD = Heal()


@pytest.fixture(autouse=True)
def deck_handler():
    deck_handler: DeckHandler = DeckHandler()
    reset_deck_handler_to_single_card_only_deck(deck_handler, SAMPLE_DISCARD_CARD)
    return deck_handler


@pytest.fixture(autouse=True)
def rich_player():
    rich_player: Player = Player()
    rich_player.energy = 100
    return rich_player


@pytest.fixture(autouse=True)
def other_players():
    other_players = [Player(), Player()]
    return other_players


def reset_deck_handler_to_single_card_only_deck(deck_handler, card):
    deck_handler.store.clear()
    deck_handler.draw_pile.clear()
    deck_handler.discard_pile.clear()
    for _ in itertools.repeat(None, 10):
        deck_handler.draw_pile.append(card)
    for _ in itertools.repeat(None, 3):
        deck_handler.store.append(deck_handler.draw_pile.draw_from())


def test_deck_handler_test_setup(deck_handler, rich_player):
    deck_handler.buy_card_from_store(0, rich_player, other_players)
    assert not len(deck_handler.store) + len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME

    reset_deck_handler_to_single_card_only_deck(deck_handler, SAMPLE_KEEP_CARD)
    assert len(deck_handler.discard_pile) == 0
    for card in deck_handler.store:
        assert isinstance(card, SAMPLE_KEEP_CARD.__class__)

    reset_deck_handler_to_single_card_only_deck(deck_handler, SAMPLE_DISCARD_CARD)
    for card in deck_handler.store:
        assert isinstance(card, SAMPLE_DISCARD_CARD.__class__)


def test_deck_handler_init(deck_handler):
    assert len(deck_handler.store) == constants.CARD_STORE_SIZE_LIMITER
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER


def test_buy_single_keep_card(deck_handler, rich_player, other_players):
    reset_deck_handler_to_single_card_only_deck(deck_handler, SAMPLE_KEEP_CARD)
    deck_handler.buy_card_from_store(0, rich_player, other_players)
    assert len(deck_handler.discard_pile) == 0
    assert rich_player.has_instance_of_card(SAMPLE_KEEP_CARD)
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER - 1


def test_buy_single_discard_card(deck_handler, rich_player, other_players):
    reset_deck_handler_to_single_card_only_deck(deck_handler, SAMPLE_DISCARD_CARD)
    deck_handler.buy_card_from_store(0, rich_player, other_players)
    assert not rich_player.has_instance_of_card(SAMPLE_DISCARD_CARD)
    assert len(deck_handler.draw_pile) == NUMBER_OF_CARDS_IN_GAME - constants.CARD_STORE_SIZE_LIMITER - 1
    assert len(deck_handler.discard_pile) == 1


def test_discard_card_from_player_hand(deck_handler, rich_player, other_players):
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME
    rich_player.add_card(SAMPLE_DISCARD_CARD)
    deck_handler.discard(SAMPLE_DISCARD_CARD, rich_player.cards)
    assert len(deck_handler) == NUMBER_OF_CARDS_IN_GAME + 1
    assert len(rich_player.cards) == 0


def test_cards_cost_energy(deck_handler, rich_player, other_players):
    initial_energy = rich_player.energy
    card_player_will_buy = deck_handler.store[1]
    deck_handler.buy_card_from_store(1, rich_player, other_players)
    assert rich_player.energy == initial_energy - card_player_will_buy.cost


def test_keep_cards_bought_are_added_to_player(deck_handler, rich_player, other_players):
    reset_deck_handler_to_single_card_only_deck(deck_handler, SAMPLE_KEEP_CARD)
    assert len(rich_player.cards) == 0
    deck_handler.buy_card_from_store(0, rich_player, other_players)
    assert len(rich_player.cards) == 1
    assert rich_player.has_instance_of_card(SAMPLE_KEEP_CARD)


def test_force_shuffle_discard_add_to_draw(deck_handler, rich_player, other_players):
    bought_cards: List[Card] = list()

    # buy all cards but the 3 in the store, reset energy to never run out for test
    for _ in range(NUMBER_OF_CARDS_IN_GAME - 3):
        rich_player.energy = 100
        deck_handler.buy_card_from_store(1, rich_player, other_players)

    assert len(deck_handler.draw_pile) == 0

    deck_handler.buy_card_from_store(0, rich_player, other_players)

    assert len(deck_handler.draw_pile) > 0


def test_auto_reshuffle(deck_handler, rich_player, other_players):
    # buy all cards but 1 and the store
    for _ in range(NUMBER_OF_CARDS_IN_GAME - (1 + constants.CARD_STORE_SIZE_LIMITER)):
        rich_player.energy = 100
        deck_handler.buy_card_from_store(1, rich_player, other_players)
    #  Now there's only one in the draw pile, and the three in the store
    assert len(deck_handler.draw_pile) == 1

    # buy all card but 1 and the store again, forcing reshuffle discard to draw pile, reset energy to never run out
    for _ in range(NUMBER_OF_CARDS_IN_GAME - (1 + constants.CARD_STORE_SIZE_LIMITER)):
        rich_player.energy = 100
        deck_handler.buy_card_from_store(0, rich_player, other_players)


def test_do_not_sell_card_to_player_with_no_energy(deck_handler, other_players):
    poor_player = Player()
    poor_player.energy = 0
    with pytest.raises(Exception) as raised_exception:
        deck_handler.buy_card_from_store(1, poor_player, other_players)
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
    reset_deck_handler_to_single_card_only_deck(deck_handler, SAMPLE_KEEP_CARD)
    deck_handler.draw_pile.clear()
    for _ in itertools.repeat(None, 7):
        deck_handler.draw_pile.add_card_to_deck(SAMPLE_DISCARD_CARD)
    deck_handler.sweep_store(test_player)
    for card in deck_handler.store:
        assert isinstance(card, SAMPLE_DISCARD_CARD.__class__)


def test_sweep_store_puts_current_cards_in_discard(deck_handler):
    test_player = Player()
    test_player.energy = constants.SWEEP_CARD_STORE_COST
    initial_cards_in_store = [deck_handler.store[0], deck_handler.store[1],
                              deck_handler.store[2]]
    deck_handler.sweep_store(test_player)
    assert len(deck_handler.discard_pile) == constants.CARD_STORE_SIZE_LIMITER
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
