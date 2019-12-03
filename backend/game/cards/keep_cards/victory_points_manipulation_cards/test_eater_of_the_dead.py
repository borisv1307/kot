from game.cards.keep_cards.victory_points_manipulation_cards.eater_of_the_dead import EaterOfTheDead

def test_eater_of_the_dead_adds_3_victory_points(player, other_players):
    EaterOfTheDead().immediate_effect(player, None)
    EaterOfTheDead().special_effect(player, other_players)
    assert player.victory_points == 3

def test_eater_of_the_dead_costs_4_energy():
    assert EaterOfTheDead().cost == 4