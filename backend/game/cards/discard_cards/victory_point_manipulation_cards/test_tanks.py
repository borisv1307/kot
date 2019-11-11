from game.cards.discard_cards.victory_point_manipulation_cards.tanks import Tanks


def test_jet_fighters_adds_4_victory_points(player):
    Tanks().immediate_effect(player, None)
    assert player.victory_points == 4


def test_jet_fighters_subtracts_3_health(player):
    player.current_health = 9
    Tanks().immediate_effect(player, None)
    assert player.current_health == 6


def test_jet_fighters_costs_4_energy():
    assert Tanks().cost == 4
