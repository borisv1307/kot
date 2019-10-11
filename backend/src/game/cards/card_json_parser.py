import json
from backend.src.game.cards.card import Card
from pathlib import Path
from typing import List

json_file_path = Path("backend/src/game/cards")

# TODO the below open statement has a problem, one version makes running this file work, while the
#  other version makes running the test work

# with open('kot_cards.json', "r") as json_file:  #  this version makes running this file work
with open('backend\\src\\game\\cards\\kot_cards.json', "r") as json_file:  # this makes the test work

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
    return __card_deck


__card_deck = __deck_json_parser(card_file)

