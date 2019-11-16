from game.cards.discard_cards.multi_manipulation_cards.nuclear_power_plant import NuclearPowerPlant


def test_jet_fighters_adds_2_victory_points(player):
    NuclearPowerPlant().immediate_effect(player, None)
    assert player.victory_points == 2


def test_jet_fighters_adds_3_health(player):
    NuclearPowerPlant().immediate_effect(player, None)
    assert player.current_health == 10


def test_jet_fighters_costs_6_energy():
    assert NuclearPowerPlant().cost == 6
