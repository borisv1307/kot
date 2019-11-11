from game.player.player import Player
from game.values.locations import Locations


def move_into_empty_tokyo(attacking_player: Player, other_players):
    if attacking_player.location == Locations.OUTSIDE and all(other_players.location == Locations.OUTSIDE):
        attacking_player.move_to_tokyo()

