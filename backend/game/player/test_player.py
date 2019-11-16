import pytest

from game.cards.card import Card
from game.player.player import Player
from game.values import constants
from game.values.locations import Locations


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


def test_player_default_health(player):
    assert player.maximum_health == constants.DEFAULT_HEALTH


def test_player_default_location(player):
    assert player.location == Locations.OUTSIDE


def test_player_can_move_to_tokyo(player):
    player.move_to_tokyo()
    assert player.location == Locations.TOKYO


def test_player_can_leave_tokyo(player):
    player.leave_tokyo()
    assert player.location == Locations.OUTSIDE


def test_player_current_health_is_maximum_health_when_created(player):
    assert player.current_health == player.maximum_health


def test_player_got_hurt_by_one(player):
    player.update_health_by(-1)
    assert player.current_health == player.maximum_health - 1


def test_player_got_hurt_by_three_and_healed_by_1(player):
    player.update_health_by(-3)
    player.update_health_by(1)
    assert player.current_health == player.maximum_health - 2


def test_player_health_can_not_exceed_max_health(player):
    player.update_health_by(1)
    assert player.current_health == player.maximum_health


def test_player_dies_when_current_health_hits_zero(player):
    player.update_health_by(-10)
    assert not player.is_alive


def test_player_starts_with_zero_victory_points(player):
    assert player.victory_points == constants.DEATH_HIT_POINT


def test_player_can_gain_victory_points(player):
    player.update_victory_points_by(10)
    assert player.victory_points == 10


def test_player_can_lose_victory_points(player):
    player.update_victory_points_by(10)
    player.update_victory_points_by(-5)
    assert player.victory_points == 5


def test_player_starts_with_zero_energy(player):
    assert player.energy == constants.DEFAULT_ENERGY_CUBE


def test_player_can_gain_energy(player):
    player.update_energy_by(3)
    assert player.energy == 3


def test_player_can_lose_energy(player):
    player.update_energy_by(7)
    player.update_energy_by(-3)
    assert player.energy == 4


def test_player_energy_cannot_go_below_zero(player):
    player.update_energy_by(2)
    player.update_energy_by(-5)
    assert player.energy == 0


def test_player_can_not_have_less_than_zero_victory_points(player):
    player.update_victory_points_by(-1)
    assert player.victory_points == 0


def test_player_add_keep_card(player):
    Card.name = "Acid Attack"
    Card.cost = 6
    Card.footnote = ""
    Card.effect = "Add [attack] to your roll"
    player.add_keep_card(Card)
    assert player.card_on_hand.get("Acid Attack") == "Add [attack] to your roll"


def test_player_remove_keep_card(player):
    Card.name = "Acid Attack"
    Card.cost = 6
    Card.footnote = ""
    Card.effect = "Add [attack] to your roll"
    player.add_keep_card(Card)
    player.remove_keep_card(Card)
    assert player.card_on_hand.get("Acid Attack", "Not-Found") == "Not-Found"
