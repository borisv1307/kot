import json
from backend.src.game.cards.card_type import CardType
from typing import List

with open('backend\\src\\game\\cards\\kot_cards.json', "r") as json_file:
    card_file = json.load(json_file)


def set_card_type(card_type):
    if str.lower(card_type) == "keep":
        return CardType.keep
    elif str.lower(card_type) == "discard":
        return CardType.discard
    else:
        return CardType.invalid


class Card(object):
    def __init__(self, name, cost, card_type, effect, footnote):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.footnote = footnote
        self.card_type = set_card_type(card_type)

    def card_details_str(self):
        return "\nname: " + self.name + "\ncost: " + str(self.cost) + "\ntype: " + str(self.card_type) + \
               "\neffect: " + self.effect + "\nfootnote: " + self.footnote

    def is_valid(self):
        try:
            assert isinstance(self.name, str)
            assert isinstance(self.cost, int)
            assert isinstance(self.effect, str)
            assert isinstance(self.card_type, CardType) and self.card_type != CardType.invalid
        except AssertionError:
            print("invalid card: " + self.card_details_str())
            return False
        return True


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
