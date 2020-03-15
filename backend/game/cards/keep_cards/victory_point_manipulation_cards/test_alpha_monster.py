from game.cards.keep_cards.victory_point_manipulation_cards.alpha_monster import AlphaMonster


def test_alpha_monster_adds_a_victory_point(player):
    original_victory_points = player.victory_points
    AlphaMonster().special_effect(player, None)
    assert player.victory_points == original_victory_points + 1
