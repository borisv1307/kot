from game.cards.keep_cards.victory_point_manipulation_cards.omnivore import Omnivore


def test_omnivore_player_add_card(player):
    Omnivore().immediate_effect(player, None)
    assert player.has_instance_of_card(Omnivore())


def test_omnivore_costs_4_energy():
    assert Omnivore().cost == 4


def test_omnivore_adds_two_stars_on_one_two_three_rolls(player):
    original_victory_points = player.victory_points
    Omnivore().special_effect(player, None)
    assert player.victory_points == original_victory_points + 2
