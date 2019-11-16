from game.cards.discard_cards.multi_manipulation_cards.tanks import Tanks
from game.values import constants


def test_jet_fighters_adds_4_victory_points(player):
    Tanks().immediate_effect(player, None)
    assert player.victory_points == 4


def test_jet_fighters_subtracts_3_health(player):
    Tanks().immediate_effect(player, None)
    assert player.current_health == constants.DEFAULT_HEALTH - 3


def test_jet_fighters_costs_4_energy():
    assert Tanks().cost == 4
