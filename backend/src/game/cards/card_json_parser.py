import json
import os
from typing import List

from backend.src.game.cards.card import Card
from backend.src.game.constants import CARDS_DIRECTORY

json_file_path = os.path.join(CARDS_DIRECTORY, 'cards\\kot_cards.json')

with open(json_file_path, "r") as json_file:

    card_file = json.load(json_file)


def __deck_json_parser(json_deck):
    deck: List[Card] = list()
    for json_obj in json_deck['kot_cards']:
        card = Card(json_obj['name'], json_obj['cost'], json_obj['card_type'],
                    json_obj['effect'], json_obj['footnote'])
        if card.is_valid():
            deck.append(card)
    return deck


def get_power_card_deck():
    return __card_deck.copy()


__card_deck = __deck_json_parser(card_file)

