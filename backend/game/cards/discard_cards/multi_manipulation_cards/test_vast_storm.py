from game.cards.discard_cards.multi_manipulation_cards.vast_storm import VastStorm
from game.values import constants


def test_vast_storm_adds_2_victory_points(player):
    VastStorm().immediate_effect(player, None)
    assert player.victory_points == 2


def test_vast_storm_subtracts_1_health(player):
    VastStorm().immediate_effect(player, None)
    assert player.current_health == constants.DEFAULT_HEALTH - 1


def test_vast_storm_costs_6_energy():
    assert VastStorm().cost == 6
