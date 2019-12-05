from game.cards.keep_cards.health_manipulation_cards.even_bigger import EvenBigger
from game.values import constants


def test_even_bigger_player_add_card(player):
    EvenBigger().immediate_effect(player, None)
    assert player.card_on_hand.get("Even Bigger")


def test_even_bigger_gains_2_max_health_when_purchased(player):
    EvenBigger().immediate_effect(player, None)
    assert player.maximum_health == constants.DEFAULT_HEALTH + 2


def test_it_has_a_child_costs_4_energy():
    assert EvenBigger().cost == 4


def test_even_bigger_player_remove_card(player):
    EvenBigger().immediate_effect(player, None)
    EvenBigger().discard_effect(player, None)
    assert not player.card_on_hand.get("Even Bigger")


def test_even_bigger_gains_losses_2_max_health_when_lost(player):
    EvenBigger().immediate_effect(player, None)
    EvenBigger().discard_effect(player, None)
    assert player.current_health == constants.DEFAULT_HEALTH

