from game.values.locations import Locations


def move_to_tokyo_if_empty(attacking_player, other_players):
    if attacking_player.location == Locations.OUTSIDE and \
            all(other_player.location == Locations.OUTSIDE for other_player in other_players):
        attacking_player.move_to_tokyo()


def yield_tokyo(yielding_player, attacking_player):
    yielding_player.leave_tokyo()
    attacking_player.move_to_tokyo()

