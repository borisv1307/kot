from typing import List

import game.cards.discard_cards.victory_point_manipulation_cards.card_collector as vpm_card_collector

import game.cards.discard_cards.victory_point_manipulation_cards as vpm_cards
from game.cards.card import Card


def get_all_cards():
    master_card_list: List[Card] = vpm_card_collector.get_list_vpm_cards("game.cards.discard_cards.victory_point_manipulation_cards.")

    return master_card_list

print(get_all_cards())