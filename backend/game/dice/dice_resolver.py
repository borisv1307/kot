import collections

from game.dice.dice import DieValue
from game.turn_actions.attack import get_attackable_players, attack_players
from game.turn_actions.player_movement import move_to_tokyo_if_empty
from game.turn_actions.heal import heal_self_from_dice
from game.cards.keep_cards.attack_manipulation_cards.spiked_tail import SpikedTail
from game.cards.keep_cards.victory_point_manipulation_cards.alpha_monster import AlphaMonster
from game.cards.keep_cards.victory_point_manipulation_cards.complete_destruction import CompleteDestruction
from game.cards.keep_cards.victory_point_manipulation_cards.urbavore import Urbavore
from game.cards.keep_cards.victory_point_manipulation_cards.gourmet import Gourmet
from game.cards.keep_cards.victory_point_manipulation_cards.omnivore import Omnivore


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
    if attacking_player.has_instance_of_card(Urbavore()):
        attack = Urbavore.attack_dice_special_effect(attacking_player, attack)
    if attacking_player.has_instance_of_card(SpikedTail()):
        attack = SpikedTail().attack_dice_special_effect(attacking_player, attack)
    attackable_players = get_attackable_players(
        attacking_player, other_players)
    attack_players(attacking_player, attackable_players, attack)
    if attack > 0:
        move_to_tokyo_if_empty(attacking_player, other_players)


def resolve_health_dice(dice_counter, player):
    health = calculate_heal_from_dice(dice_counter)
    heal_self_from_dice(player, health)


def resolve_all_other_dice(dice_counter, player):
    victory_points = calculate_victory_points_from_dice(dice_counter)
    energy = calculate_energy_from_dice(dice_counter)
    player.update_victory_points_by(victory_points)
    player.update_energy_by(energy)


def card_based_dice_actions(dice_counter, player, other_players):
    if dice_counter[DieValue.ONE] >= 3 and player.has_instance_of_card(Gourmet()):
        Gourmet().special_effect(player, other_players)
    if dice_counter[DieValue.ONE] >= 1 and dice_counter[DieValue.TWO] >= 1 and dice_counter[DieValue.THREE] >= 1 and player.has_instance_of_card(Omnivore()):
        Omnivore().special_effect(player, other_players)
    if dice_counter[DieValue.ONE] >= 1 and dice_counter[DieValue.TWO] >= 1 and dice_counter[DieValue.THREE] >= 1 and \
            dice_counter[DieValue.HEAL] >= 1 and dice_counter[DieValue.ATTACK] >= 1 and dice_counter[DieValue.ENERGY] >= 1 and \
            player.has_instance_of_card(CompleteDestruction()):
        CompleteDestruction().special_effect(player, other_players)
    if dice_counter[DieValue.ATTACK] >= 1 and player.has_instance_of_card(AlphaMonster()):
        AlphaMonster().special_effect(player, other_players)


def dice_resolution(dice, player, other_players):
    dice_counter = get_dice_count(dice)
    resolve_all_other_dice(dice_counter, player)
    card_based_dice_actions(dice_counter, player, other_players)
    resolve_health_dice(dice_counter, player)
    resolve_attack_dice(dice_counter, player, other_players)
