from game.cards.keep_cards.victory_point_manipulation_cards.urbavore import Urbavore
from game.values import locations


def test_urbavore_player_add_card(player):
    Urbavore().immediate_effect(player, None)
    assert player.card_on_hand.get("Urbavore")


def test_urbavore_costs_4_energy():
    assert Urbavore().cost == 4


def test_urbavore_gain_2_star(player):
    player.victory_points = 4
    player.location = locations.Locations.TOKYO
    Urbavore().immediate_effect(player, None)
    Urbavore().special_effect(player, None)
    assert player.victory_points == 5
