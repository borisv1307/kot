from game.cards.keep_cards.health_manipulation_cards.even_bigger import EvenBigger
from game.values import constants


def test_even_bigger_player_add_card(player):
    EvenBigger().immediate_effect(player, None)
    assert player.card_on_hand.get(
        "Even Bigger") == "+2[health] when you buy this card.maximum [health] increased to 12 as long as you own this card"


def test_even_bigger_costs_4_energy():
    assert EvenBigger().cost == 4


def test_even_bigger_change_maximum_health(player):
    player.maximum_health = constants.DEFAULT_HEALTH
    EvenBigger().immediate_effect(player, None)
    EvenBigger().special_effect(player, None)
    assert player.maximum_health == 12


def test_even_bigger_plus_2_health(player):
    player.maximum_health = constants.DEFAULT_HEALTH
    EvenBigger().immediate_effect(player, None)
    EvenBigger().special_effect(player, None)
    assert player.current_health == 12
