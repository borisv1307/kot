from game.cards.discard_cards.victory_point_manipulation_cards.heal import Heal


def test_heal_adds_2_health(player):
    player.current_health = 7
    Heal().immediate_effect(player, None)
    assert player.current_health == 9


def test_heal_costs_3_energy():
    assert Heal().cost == 3
