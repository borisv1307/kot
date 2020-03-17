from game.cards.keep_cards.victory_point_manipulation_cards.rooting_for_the_underdog import RootingForTheUnderdog
from game.player.player import Player
from game.values.constants import DEATH_HIT_POINT


def test_if_has_min_victory_points_gain_one_point():
    card_holder = Player()
    playerA = Player()
    playerB = Player()
    playerC = Player()
    playerA.update_victory_points_by(3)
    playerB.update_victory_points_by(4)
    playerC.update_victory_points_by(5)
    RootingForTheUnderdog().special_effect(
        card_holder, [playerA, playerB, playerC])
    assert card_holder.victory_points == DEATH_HIT_POINT + 1


def test_if_does_not_have_min_victory_points_gain_no_point():
    card_holder = Player()
    playerA = Player()
    playerB = Player()
    playerC = Player()
    card_holder.update_victory_points_by(3)
    playerA.update_victory_points_by(3)
    playerB.update_victory_points_by(4)
    playerC.update_victory_points_by(5)
    RootingForTheUnderdog().special_effect(
        card_holder, [playerA, playerB, playerC])
    assert card_holder.victory_points == 3
