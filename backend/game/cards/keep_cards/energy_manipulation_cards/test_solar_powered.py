from game.cards.keep_cards.energy_manipulation_cards.solar_powered import SolarPowered
from game.values import constants


def test_solar_powered_player_add_card(player):
    SolarPowered().immediate_effect(player, None)
    assert player.card_on_hand.get("Solar Powered")


def test_solar_powered_costs_4_energy():
    assert SolarPowered().cost == 4


def test_solar_powered_gain_1_star_when_energy_is_0(player):
    player.energy = constants.DEATH_HIT_POINT
    SolarPowered().immediate_effect(player, None)
    SolarPowered().special_effect(player, None)
    assert player.energy == 1
