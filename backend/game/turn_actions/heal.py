from game.player.player import Player
import game.values.locations as locations


def heal_self_from_dice(player_being_healed: Player, health_points_to_add):
    if player_being_healed.location == locations.Locations.OUTSIDE:
        player_being_healed.update_health_by(health_points_to_add)

