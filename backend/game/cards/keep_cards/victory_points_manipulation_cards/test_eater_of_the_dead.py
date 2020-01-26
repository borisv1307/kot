from game.cards.keep_cards.victory_points_manipulation_cards.eater_of_the_dead import EaterOfTheDead


def test_eater_of_the_dead_player_add_card(player):
    EaterOfTheDead().immediate_effect(player, None)
    assert player.has_instance_of_card(EaterOfTheDead())


def test_eater_of_the_dead_costs_4_energy():
    assert EaterOfTheDead().cost == 4
