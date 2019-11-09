from game.locations import Locations
from game.newcards.discard_cards.victory_point_manipulation_cards.drop_from_high_altitude import DropFromHighAltitude


def test_drop_from_high_altitude_adds_2_victory_points(player):
    DropFromHighAltitude().immediate_effect(player, None)
    assert player.victory_points == 2


def test_drop_from_high_altitude_costs_5_energy():
    assert DropFromHighAltitude().cost == 5


def test_drop_from_high_altitude_location_tokyo():
    assert DropFromHighAltitude().location == Locations.OUTSIDE
