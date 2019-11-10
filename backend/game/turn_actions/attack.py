def is_attackable(attacking_player_location, other_player):
    if attacking_player_location != other_player.location:
        return True
    else:
        return False


def get_attackable_players(attacking_player, other_players):
    attackable_players = []
    attacking_player_location = attacking_player.location
    for other_player in other_players:
        if is_attackable(attacking_player_location, other_player):
            attackable_players.append(other_player)
    return attackable_players


def attack_players(attackable_players, attack_value=-1):
    for attacked_player in attackable_players:
        attacked_player.update_health_by(attack_value)
