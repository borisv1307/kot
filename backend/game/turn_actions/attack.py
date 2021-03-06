from game.cards.keep_cards.attack_manipulation_cards.nova_breath import NovaBreath
from game.player.player import Player
from game.turn_actions.player_movement import take_tokyo_on_kill
from game.values.locations import Locations


def is_attackable(attacking_player, other_player):
    if attacking_player.location != other_player.location:
        if Locations.OUTSIDE in {attacking_player.location,
                                 other_player.location}:
            return True
    return False


def get_attackable_players(attacking_player: Player, other_players, is_dice_roll=True):
    attackable_players = []

    if is_dice_roll and attacking_player.has_instance_of_card(NovaBreath()):
        return other_players
    else:
        for other_player in other_players:
            if is_attackable(attacking_player, other_player):
                attackable_players.append(other_player)
        return attackable_players


def attack_players(attacking_player, attackable_players, attack_value=1):
    for attacked_player in attackable_players:
        attacked_player.update_health_by(attack_value * -1)
        if not attacked_player.is_alive:
            take_tokyo_on_kill(attacking_player, attacked_player)
        elif attacked_player.is_in_tokyo() and attack_value > 0:
            attacked_player.allowed_to_yield = True
