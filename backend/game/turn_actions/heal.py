import game.player.player as player
import game.values.locations as locations


def heal_self(player_healing: player.Player, health_points_to_add):
    if player_healing.location is not locations.Locations.TOKYO:
        player_healing.update_health_by(health_points_to_add)
