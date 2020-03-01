from game.cards.keep_cards.victory_point_manipulation_cards.gourmet import Gourmet


def test_gourmet_player_add_card(player):
    Gourmet().immediate_effect(player, None)
    assert player.has_instance_of_card(Gourmet())


def test_gourmet_costs_4_energy():
    assert Gourmet().cost == 4


def test_gourmet_adds_two_stars_on_three_ones_rolled(player):
    original_victory_points = player.victory_points
    Gourmet().special_effect(player, None)
    assert player.victory_points == original_victory_points + 2
