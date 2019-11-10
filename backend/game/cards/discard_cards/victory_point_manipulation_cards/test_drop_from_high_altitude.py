from game.cards.discard_cards.victory_point_manipulation_cards.drop_from_high_altitude import DropFromHighAltitude
from game.values.locations import Locations


def test_drop_from_high_altitude_adds_2_victory_points(player):
    DropFromHighAltitude().immediate_effect(player, None)
    assert player.victory_points == 2


def test_drop_from_high_altitude_costs_5_energy():
    assert DropFromHighAltitude().cost == 5


def test_drop_from_high_altitude_location_tokyo():
    assert DropFromHighAltitude().location == Locations.OUTSIDE


def test_drop_from_high_altitude_location_outside_tokyo(five_players):
    for player in five_players:
        if player.location == Locations.OUTSIDE:
            player.move_to_tokyo()
            break
    DropFromHighAltitude().immediate_effect(None, five_players)
    assert all(other_players.location == Locations.OUTSIDE
               for other_players in five_players)
