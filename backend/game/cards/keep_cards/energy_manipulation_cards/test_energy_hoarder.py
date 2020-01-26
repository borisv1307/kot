from game.cards.keep_cards.energy_manipulation_cards.energy_hoarder import EnergyHoarder


def test_energy_hoarder_player_add_card(player):
    EnergyHoarder().immediate_effect(player, None)
    assert player.has_instance_of_card(EnergyHoarder())


def test_energy_hoarder_costs_4_energy():
    assert EnergyHoarder().cost == 3


def test_energy_hoarder_gain_2_star(player):
    player.energy = 13
    player.add_card(EnergyHoarder())
    EnergyHoarder().special_effect(player, None)
    assert player.victory_points == 2
