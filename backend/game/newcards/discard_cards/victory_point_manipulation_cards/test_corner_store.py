from game.newcards.discard_cards.victory_point_manipulation_cards.corner_store import CornerStore


def test_corner_store_adds_1_victory_points(player):
    CornerStore().immediate_effect(player, None)
    assert player.victory_points == 1


def test_corner_store_costs_3_energy():
    assert CornerStore().cost == 3
