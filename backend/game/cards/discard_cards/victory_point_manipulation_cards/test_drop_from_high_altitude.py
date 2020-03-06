from game.cards.discard_cards.victory_point_manipulation_cards.drop_from_high_altitude import DropFromHighAltitude
from game.player.player import Player
from game.values.locations import Locations


def test_drop_from_high_altitude_adds_2_victory_points(player):
    DropFromHighAltitude().immediate_effect(player, Player())
    assert player.victory_points == 2


def test_drop_from_high_altitude_costs_5_energy():
    assert DropFromHighAltitude().cost == 5


def test_drop_from_high_altitude_location_tokyo(player):
    DropFromHighAltitude().immediate_effect(player)
    assert player.location == Locations.TOKYO


def test_drop_from_high_altitude_force_other_player_out(player):
    other_player = Player()
    other_player.move_to_tokyo()
    DropFromHighAltitude().immediate_effect(player, other_player)
    assert other_player.location == Locations.OUTSIDE
