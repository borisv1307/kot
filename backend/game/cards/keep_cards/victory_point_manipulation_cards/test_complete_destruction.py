from game.cards.keep_cards.victory_point_manipulation_cards.complete_destruction import CompleteDestruction


def test_complete_destruction_player_add_card(player):
    CompleteDestruction().immediate_effect(player, None)
    assert player.has_instance_of_card(CompleteDestruction())


def test__complete_destruction_costs_3_energy():
    assert CompleteDestruction().cost == 3


def test_CompleteDestruction_adds_nine_victory_points(player):
    original_victory_points = player.victory_points
    CompleteDestruction().special_effect(player, None)
    assert player.victory_points == original_victory_points + 9
