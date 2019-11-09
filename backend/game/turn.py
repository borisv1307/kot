import collections

from game import constants
from game.dice.dice import DieValue
from game.locations import Locations


def get_dice_count(dice):
    return collections.Counter(dice)


def calculate_victory_points_from_dice(dice_counter):
    victory_points = 0
    victory_dice = [DieValue.ONE, DieValue.TWO, DieValue.THREE]
    for victory_die in victory_dice:
        die_count = dice_counter[victory_die]
        leftover_dice = die_count - 3
        if leftover_dice >= 0:
            victory_points += (victory_die.value + leftover_dice)
    return victory_points


def calculate_energy_from_dice(dice_counter):
    return dice_counter[DieValue.ENERGY]


def calculate_attack_from_dice(dice_counter):
    return dice_counter[DieValue.ATTACK]


def calculate_heal_from_dice(dice_counter):
    return dice_counter[DieValue.HEAL]


def dice_resolution(dice, player):
    dice_counter = get_dice_count(dice)
    victory_points = calculate_victory_points_from_dice(dice_counter)
    health = calculate_heal_from_dice(dice_counter)
    attack = calculate_attack_from_dice(dice_counter)
    energy = calculate_energy_from_dice(dice_counter)
    return victory_points, health, attack, energy


def if_attackable(attacking_player_location, other_player):
    if attacking_player_location != other_player.location:
        return True
    else:
        return False


def get_attackable_players(attacking_player, other_players):
    attackable_players = []
    attacking_player_location = attacking_player.location
    for other_player in other_players:
        if if_attackable(attacking_player_location, other_player):
            attackable_players.append(other_player)
    return attackable_players


def attack_players(attackable_players, attack_value=-1):
    for attacked_player in attackable_players:
        attacked_player.update_health_by(attack_value)
