from game.values.locations import Locations
from game.turn_actions.player_movement import move_to_tokyo_if_empty, yield_tokyo


def is_attackable(attacking_player_location, other_player):
    if attacking_player_location != other_player.location and \
            (attacking_player_location == Locations.OUTSIDE or other_player.location == Locations.OUTSIDE):
        return True
    else:
        return False


def get_attackable_players(attacking_player, other_players):
    attackable_players = []
    attacking_player_location = attacking_player.location
    for other_player in other_players:
        if is_attackable(attacking_player_location, other_player):
            attackable_players.append(other_player)
    if attacking_player.location == Locations.OUTSIDE and attackable_players.__len__() < 1:
        move_to_tokyo_if_empty(attacking_player, other_players)
    return attackable_players


def attack_players(attacking_player, attackable_players, attack_value=1):
    for attacked_player in attackable_players:
        attacked_player.update_health_by(attack_value * -1)
        if attacked_player.is_alive is False and attacked_player.location == Locations.TOKYO:
            yield_tokyo(attacked_player, attacking_player)
