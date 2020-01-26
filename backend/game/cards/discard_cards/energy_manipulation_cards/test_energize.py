from game.cards.discard_cards.energy_manipulation_cards.energize import Energize
from game.values import constants


def test_energize_adds_9_energy_cubes(player):
    Energize().immediate_effect(player, None)
    assert player.energy == constants.DEFAULT_ENERGY_CUBE + 9


def test_energize_costs_8_energy():
    assert Energize().cost == 8
