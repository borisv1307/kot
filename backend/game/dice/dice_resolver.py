import collections

from game.dice.dice import DieValue
from game.turn_actions.attack import get_attackable_players, attack_players
from game.turn_actions.player_movement import move_to_tokyo_if_empty
from game.turn_actions.heal import heal_self_from_dice


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


def resolve_attack_dice(dice_counter, attacking_player, other_players):
    attack = calculate_attack_from_dice(dice_counter)
    attackable_players = get_attackable_players(
        attacking_player, other_players)
    attack_players(attacking_player, attackable_players, attack)
    if attack > 1:
        move_to_tokyo_if_empty(attacking_player, other_players)


def resolve_health_dice(dice_counter, player):
    health = calculate_heal_from_dice(dice_counter)
    heal_self_from_dice(player, health)


def resolve_all_other_dice(dice_counter, player):
    victory_points = calculate_victory_points_from_dice(dice_counter)
    energy = calculate_energy_from_dice(dice_counter)
    player.update_victory_points_by(victory_points)
    player.update_energy_by(energy)


def dice_resolution(dice, player, other_players):
    dice_counter = get_dice_count(dice)
    resolve_all_other_dice(dice_counter, player)
    resolve_health_dice(dice_counter, player)
    resolve_attack_dice(dice_counter, player, other_players)
