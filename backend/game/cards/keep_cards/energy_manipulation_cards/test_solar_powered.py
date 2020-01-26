from game.cards.keep_cards.energy_manipulation_cards.solar_powered import SolarPowered
from game.player.player import Player


def test_solar_powered_costs_4_energy():
    assert SolarPowered().cost == 4


def test_solar_powered_gain_1_star_when_energy_is_0(player):
    player.energy = 0
    SolarPowered().immediate_effect(player, None)
    SolarPowered().special_effect(player, None)
    assert player.energy == 1
