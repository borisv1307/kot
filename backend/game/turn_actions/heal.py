from game.player.player import Player
import game.values.locations as locations


def heal_self_from_dice(player_being_healed: Player, health_points_to_add):
    if player_being_healed.location is not locations.Locations.TOKYO:
        player_being_healed.update_health_by(health_points_to_add)


def heal_self_no_tokyo_restriction(player_being_healed: Player, health_points_to_add):
    player_being_healed.update_health_by(health_points_to_add)
