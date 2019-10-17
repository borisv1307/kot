import pytest

from backend.src.game.newcards.discard_cards.victory_point_manipulation_cards.apartment_building import \
    ApartmentBuilding
from backend.src.game.player import Player


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


def test_apartment_building_adds_3_victory_points(player):
    ApartmentBuilding().immediate_effect(player, None)
    assert player.victory_points == 3


def test_apartment_building_costs_5_energy():
    assert ApartmentBuilding().cost == 5
