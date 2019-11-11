from game.cards.discard_cards.multi_point_manipulation_cards.national_guard import NationalGuard


def test_jet_fighters_adds_2_victory_points(player):
    NationalGuard().immediate_effect(player, None)
    assert player.victory_points == 2


def test_jet_fighters_subtracts_2_health(player):
    player.current_health = 8
    NationalGuard().immediate_effect(player, None)
    assert player.current_health == 6


def test_jet_fighters_costs_3_energy():
    assert NationalGuard().cost == 3
