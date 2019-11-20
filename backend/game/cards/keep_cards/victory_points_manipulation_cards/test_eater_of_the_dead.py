from game.cards.keep_cards.victory_points_manipulation_cards.eater_of_the_dead import EaterOfTheDead
from game.values import constants


def test_player_holds_eater_of_the_dead(player):
    EaterOfTheDead().immediate_effect(player, None)
    assert player.get_card_at_index(0).name == "Eater of the Dead"


def test_eater_of_the_dead_special_effect(player, five_players):
    EaterOfTheDead().immediate_effect(player, None)
    five_players[0].current_health = constants.DEATH_HIT_POINT
    EaterOfTheDead().special_effect(player, five_players)
    assert player.victory_points == 3
