from game.cards.discard_cards.multi_manipulation_cards.nuclear_power_plant import NuclearPowerPlant
from game.values import constants


def test_nuclear_power_adds_2_victory_points(player):
    NuclearPowerPlant().immediate_effect(player, None)
    assert player.victory_points == 2


def test_nuclear_power_adds_3_health(player):
    player.current_health = player.current_health - 3
    NuclearPowerPlant().immediate_effect(player, None)
    assert player.current_health == constants.DEFAULT_HEALTH


def test_nuclear_power_costs_6_energy():
    assert NuclearPowerPlant().cost == 6


def test_type_is_discard():
    assert NuclearPowerPlant().type == "Discard"
