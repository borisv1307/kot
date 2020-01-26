from game.cards.keep_cards.health_manipulation_cards.it_has_a_child import ItHasAChild
from game.player.player import Player
from game.values.locations import Locations


def test_it_has_a_child_player_add_card(player):
    ItHasAChild().immediate_effect(player, None)
    assert player.has_instance_of_card(ItHasAChild())


def test_it_has_a_child_costs_7_energy():
    assert ItHasAChild().cost == 7


def test_it_has_a_child_discards_all_cards_when_health_is_0(player):
    player.current_health = 0
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().special_effect(player, None)
    assert len(player.cards) == 0


def test_it_has_a_child_loses_all_stars_when_health_is_0(player):
    player.victory_points = 5
    ItHasAChild().immediate_effect(player, None)
    player.current_health = 0
    ItHasAChild().special_effect(player, None)
    assert player.victory_points == 0


def test_it_has_a_child_gains_10_health_when_health_is_0(player):
    player.current_health = 0
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().special_effect(player, None)
    assert player.current_health == 10


def test_it_has_a_child_moves_outside_tokyo_when_played(player):
    player.move_to_tokyo()
    player.current_health = 0
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().special_effect(player, None)
    assert player.location == Locations.OUTSIDE


def test_it_has_a_child_no_affect_when_health_above_zero(player):
    player.current_health = 2
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().special_effect(player, None)
    assert len(player.cards) > 0
