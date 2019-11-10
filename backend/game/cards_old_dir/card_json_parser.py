import json
import os
from typing import List

from game.cards_old_dir.old_card import Old_Card


CARDS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(CARDS_DIRECTORY, 'kot_cards.json')

with open(json_file_path, "r") as json_file:

    card_file = json.load(json_file)


def __deck_json_parser(json_deck):
    deck: List[Old_Card] = list()
    for json_obj in json_deck['kot_cards']:
        card = Old_Card(json_obj['name'], json_obj['cost'], json_obj['card_type'],
                        json_obj['effect'], json_obj['footnote'])
        if card.is_valid():
            deck.append(card)
    return deck


def get_power_card_deck():
    return __card_deck.copy()


__card_deck = __deck_json_parser(card_file)
