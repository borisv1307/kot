from game.cards.discard_cards.health_manipulation_cards.heal import Heal
from game.values import constants


def test_heal_adds_2_health(player):
    player.current_health = player.current_health - 2
    Heal().immediate_effect(player, None)
    assert player.current_health == constants.DEFAULT_HEALTH


def test_heal_costs_3_energy():
    assert Heal().cost == 3


def test_type_is_discard():
    assert Heal().type == "Discard"
