from game.cards.keep_cards.health_manipulation_cards.it_has_a_child import ItHasAChild
from game.values import constants


def test_it_has_a_child_player_add_card(player):
    ItHasAChild().immediate_effect(player, None)
    assert player.card_on_hand.get("It Has a Child")


def test_it_has_a_child_player_remove_card(player):
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().discard_effect(player, None)
    assert not player.card_on_hand.get("It Has a Child")


def test_it_has_a_child_costs_7_energy():
    assert ItHasAChild().cost == 7


def test_it_has_a_child_discards_all_cards_when_health_is_0(player):
    player.energy = constants.ZERO_ENERGY
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().special_effect(player, None)
    assert player.card_on_hand.get("It Has a Child", "Not-Found") == "Not-Found"


def test_it_has_a_child_loses_all_stars_when_health_is_0(player):
    player.energy = constants.ZERO_ENERGY
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().special_effect(player, None)
    assert player.victory_points == 0


def test_it_has_a_child_gains_10_health_when_health_is_0(player):
    player.energy = constants.ZERO_ENERGY
    ItHasAChild().immediate_effect(player, None)
    ItHasAChild().special_effect(player, None)
    assert player.current_health == 10
