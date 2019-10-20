import collections

from backend.src.game import constants
from backend.src.game.locations import Locations
from backend.src.game.dice import DieValue


def get_dice_count(dice):
    return collections.counter(dice)


def resolve_victory_points_dice(dice_counter):
    victory_points = 0
    for die, die_count in dice_counter.items():
        if die in [DieValue.ONE, DieValue.TWO, DieValue.THREE]:
            leftover_dice = die_count - 3
            if leftover_dice >= 0:
                victory_points += (die.value + leftover_dice)
    return victory_points


def resolve_energy_dice(dice_counter):
    energy = 0
    if DieValue.ENERGY in dice_counter:
        energy = dice_counter[DieValue.ENERGY]
    return energy


def resolve_attack_dice(dice_counter):
    attack = 0
    if DieValue.ATTACK in dice_counter:
        attack = dice_counter[DieValue.ATTACK]
    return attack
