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
    attack_rolled = 3
    attack = Urbavore().attack_dice_special_effect(player, attack_rolled)
    assert attack == attack_rolled + 1


def test_urbavore_adding_to_attack_when_in_tokyo_and_attack_is_zero(player):
    player.location = locations.Locations.TOKYO
    attack_rolled = 0
    attack = Urbavore().attack_dice_special_effect(player, attack_rolled)
    assert attack == attack_rolled


def test_urbavore_adding_to_attack_whe_not_in_tokyo_and_attack_greater_than_one(player):
    player.location = locations.Locations.OUTSIDE
    attack_rolled = 2
    attack = Urbavore().attack_dice_special_effect(player, attack_rolled)
    assert attack == attack_rolled


def test_urbavore_adding_to_attack_when_not_in_tokyo_and_attack_is_zero(player):
    player.location = locations.Locations.OUTSIDE
    attack_rolled = 0
    attack = Urbavore().attack_dice_special_effect(player, attack_rolled)
    assert attack == attack_rolled
