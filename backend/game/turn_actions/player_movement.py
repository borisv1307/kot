from game.values.locations import Locations


def tokyo_is_empty(attacking_player, other_players):
    if attacking_player.location != Locations.OUTSIDE:
        return False
    for player in other_players:
        if player.location != Locations.OUTSIDE:
            return False
    return True


def move_to_tokyo_if_empty(attacking_player, other_players):
    if tokyo_is_empty(attacking_player, other_players):
        attacking_player.move_to_tokyo()
        attacking_player.update_victory_points_by(1)


def take_tokyo_on_kill(attacking_player, murdered_player):
    if attacking_player.location == Locations.OUTSIDE and murdered_player.location != Locations.OUTSIDE:
        yield_tokyo(murdered_player, attacking_player)


def yield_tokyo(yielding_player, attacking_player):
    yielding_player.leave_tokyo()
    attacking_player.move_to_tokyo()
    attacking_player.update_victory_points_by(1)
