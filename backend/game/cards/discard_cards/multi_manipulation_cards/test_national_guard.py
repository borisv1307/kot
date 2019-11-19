from game.cards.discard_cards.multi_manipulation_cards.national_guard import NationalGuard
from game.values import constants


def test_national_guard_adds_2_victory_points(player):
    NationalGuard().immediate_effect(player, None)
    assert player.victory_points == 2


def test_national_guard_subtracts_2_health(player):
    NationalGuard().immediate_effect(player, None)
    assert player.current_health == constants.DEFAULT_HEALTH - 2


def test_national_guard_costs_3_energy():
    assert NationalGuard().cost == 3
