from game.cards.discard_cards.health_manipulation_cards.heal import Heal
from game.values import constants


def test_heal_adds_2_health(player):
    player.current_health = constants.DEFAULT_HEALTH
    Heal().immediate_effect(player, None)
    assert player.current_health == 10


def test_heal_costs_3_energy():
    assert Heal().cost == 3
