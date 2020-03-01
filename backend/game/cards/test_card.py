from game.cards.discard_card import DiscardCard
from game.cards.keep_cards.attack_manipulation_cards.nova_breath import NovaBreath
from game.values.constants import CARD_FOOTNOTE_KEY, CARD_EFFECT_KEY, CARD_COST_KEY, CARD_NAME_KEY, CARD_TYPE_KEY

title = "Test title"
cost = 100
description = "Lose 100 energy"
footnote = "Why would you buy this?"


class PhonyCard(DiscardCard):
    def __init__(self):
        super().__init__(title, cost, description, footnote)

    def immediate_effect(self, player_that_bought_the_card, other_players):
        pass


def test_card_dict():
    card = PhonyCard()
    actual_dict = card.to_dict()
    assert actual_dict.get(CARD_NAME_KEY) == title
    assert actual_dict.get(CARD_COST_KEY) == 100
    assert actual_dict.get(CARD_EFFECT_KEY) == description
    assert actual_dict.get(CARD_FOOTNOTE_KEY) == footnote
    assert actual_dict.get(CARD_TYPE_KEY) == "Discard"


def test_card_json():
    card = PhonyCard()
    json = card.to_json()
    assert json == '{{"{}": "Test title", "{}": 100, "{}": "Discard", "{}": "Lose 100 energy", "{}": ' \
                   '"Why would you buy this?"}}'.format(CARD_NAME_KEY, CARD_COST_KEY, CARD_TYPE_KEY, CARD_EFFECT_KEY,
                                                        CARD_FOOTNOTE_KEY)


def test_methods_carry_to_inherited_classes():
    card = NovaBreath()
    assert card.to_dict().get("effect")

    assert card.to_json() == '{{"{}": "Nova Breath", "{}": 7, "{}": "Keep", "{}": "Your [attack] Smash all other ' \
                             'monsters", ' '"{}": null}}'.format(CARD_NAME_KEY, CARD_COST_KEY, CARD_TYPE_KEY,
                                                                 CARD_EFFECT_KEY, CARD_FOOTNOTE_KEY)
