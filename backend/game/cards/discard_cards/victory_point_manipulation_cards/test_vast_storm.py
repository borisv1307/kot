from game.cards.discard_cards.victory_point_manipulation_cards.vast_storm import VastStorm


def test_vast_storm_adds_2_victory_points(player):
    VastStorm().immediate_effect(player, None)
    assert player.victory_points == 2


def test_vast_storm_subtracts_3_health(player):
    player.current_health = 8
    VastStorm().immediate_effect(player, None)
    assert player.current_health == 7


def test_vast_storm_costs_6_energy():
    assert VastStorm().cost == 6
