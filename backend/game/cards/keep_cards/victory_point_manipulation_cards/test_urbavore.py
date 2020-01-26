from game.cards.keep_cards.victory_point_manipulation_cards.urbavore import Urbavore
from game.values import locations


def test_urbavore_costs_4_energy():
    assert Urbavore().cost == 4


def test_urbavore_gain_1_star_when_in_tokyo(player):
    player.location = locations.Locations.TOKYO
    Urbavore().special_effect(player, None)
    assert player.victory_points == 1


def test_urbavore_gains_no_stars_when_not_in_tokyo(player):
    player.location = locations.Locations.OUTSIDE
    Urbavore().special_effect(player, None)
    assert player.victory_points == 0


def test_urbavore_adding_to_attack_when_in_tokyo_and_attack_greater_than_one(player):
    player.location = locations.Locations.TOKYO
    attack = Urbavore().attack_dice_special_effect(player, 3)
    assert attack == 4


def test_urbavore_adding_to_attack_when_in_tokyo_and_attack_is_zero(player):
    player.location = locations.Locations.TOKYO
    attack = Urbavore().attack_dice_special_effect(player, 0)
    assert attack == 0


def test_urbavore_adding_to_attack_when_in_tokyo_and_attack_greater_than_one(player):
    player.location = locations.Locations.TOKYO
    attack = Urbavore().attack_dice_special_effect(player, 3)
    assert attack == 4


def test_urbavore_adding_to_attack_when_not_in_tokyo_and_attack_is_greater_than_one(player):
    player.location = locations.Locations.OUTSIDE
    attack = Urbavore().attack_dice_special_effect(player, 2)
    assert attack == 2
