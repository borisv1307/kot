from game.cards.discard_cards.victory_point_manipulation_cards.drop_from_high_altitude import DropFromHighAltitude
from game.values.locations import Locations


def test_drop_from_high_altitude_adds_2_victory_points(player, five_players):
    DropFromHighAltitude().immediate_effect(player, five_players)
    assert player.victory_points == 2


def test_drop_from_high_altitude_costs_5_energy():
    assert DropFromHighAltitude().cost == 5


def test_drop_from_high_altitude_location_tokyo(player, five_players):
    DropFromHighAltitude().immediate_effect(player, five_players)
    assert player.location == Locations.TOKYO


def test_drop_from_high_altitude_location_outside_tokyo(player, five_players):
    for other_players in five_players:
        if other_players.location == Locations.OUTSIDE:
            other_players.move_to_tokyo()
            break
    DropFromHighAltitude().immediate_effect(player, five_players)
    assert all(other_players.location == Locations.OUTSIDE
               for other_players in five_players)
