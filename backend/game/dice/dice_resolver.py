import collections

from game.dice.dice import DieValue
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


def dice_resolution(dice, player):
    dice_counter = get_dice_count(dice)
    victory_points = calculate_victory_points_from_dice(dice_counter)
    health = calculate_heal_from_dice(dice_counter)
    heal_self_from_dice(player, health)
    attack = calculate_attack_from_dice(dice_counter)
    energy = calculate_energy_from_dice(dice_counter)
    return victory_points, health, attack, energy


