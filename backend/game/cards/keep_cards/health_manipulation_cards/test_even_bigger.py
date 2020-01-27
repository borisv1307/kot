import pytest

from game.cards.keep_cards.health_manipulation_cards.even_bigger import EvenBigger
from game.player.player import Player
from game.values import constants


@pytest.fixture(autouse=True)
def player():
    player = Player()
    player.add_card(EvenBigger())
    EvenBigger.immediate_effect(None, player, None)
    return player


def test_even_bigger_gains_2_max_health_when_purchased(player):
    assert player.maximum_health == constants.DEFAULT_HEALTH + 2


def test_even_bigger_gains_2_current_health_when_purchased(player):
    assert player.current_health == constants.DEFAULT_HEALTH + 2


def test_even_bigger_costs_4_energy():
    assert EvenBigger().cost == 4


def test_even_bigger_gains_losses_2_max_health_when_lost(player):
    EvenBigger().discard_effect(player, None)
    assert player.maximum_health == constants.DEFAULT_HEALTH


def test_even_bigger_gains_losses_2_current_health_when_lost(player):
    EvenBigger().discard_effect(player, None)
    assert player.current_health == constants.DEFAULT_HEALTH


def test_damaged_player_does_not_lose_health_when_discarded(player):
    player.current_health = 8
    player.remove_card(EvenBigger())
    EvenBigger.discard_effect(None, player, None)
    assert player.maximum_health == constants.DEFAULT_HEALTH and player.current_health == 8

#TODO attach discard method to turn logic