import game.cards.discard_cards.victory_point_manipulation_cards.card_collector as vpm_card_collector
from typing import List
from game.cards.card import Card


DIRECTORIES_TO_SEARCH_FOR_CARDS = "game.cards.discard_cards.victory_point_manipulation_cards"


def get_all_cards():

    master_card_list: List[Card] = []

    master_card_list.extend(vpm_card_collector.get_list_vpm_cards(DIRECTORIES_TO_SEARCH_FOR_CARDS))

    return master_card_list
