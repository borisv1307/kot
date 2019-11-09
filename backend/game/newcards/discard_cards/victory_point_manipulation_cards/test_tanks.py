from game.newcards.discard_cards.victory_point_manipulation_cards.tanks import Tanks


def test_jet_fighters_adds_2_victory_points(player):
    Tanks().immediate_effect(player, None)
    assert player.victory_points == 2


def test_jet_fighters_subtracts_3_health(player):
    player.update_health_by(10)
    Tanks().immediate_effect(player, None)
    assert player.current_health == 7


def test_jet_fighters_costs_4_energy():
    assert Tanks().cost == 4
