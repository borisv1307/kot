from game.newcards.discard_cards.victory_point_manipulation_cards.jet_fighters import JetFighters


def test_jet_fighters_adds_5_victory_points(player):
    JetFighters().immediate_effect(player, None)
    assert player.victory_points == 5


def test_jet_fighters_subtracts_4_health(player):
    player.update_health_by(10)
    JetFighters().immediate_effect(player, None)
    assert player.current_health == 6


def test_jet_fighters_costs_5_energy():
    assert JetFighters().cost == 5
