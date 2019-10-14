from backend.src.game.cards import card_json_parser as parser
from backend.src.game.cards.card_type import CardType
from backend.test.game.cards_test import mock_card_json as mock_cards


def test_deck_multiple_cards():
    test_deck = parser.__deck_json_parser(mock_cards.mock_json_2_cards)
    assert len(test_deck) == 2

    commuter_card = test_deck[0]
    assert commuter_card.name == "Commuter Train" \
        and commuter_card.cost == 4 \
        and commuter_card.card_type == CardType.discard \
        and commuter_card.effect == "+ 2[Star]" \
        and commuter_card.footnote == ""

    camo_card = test_deck[1]
    assert camo_card.name == "Camouflage" \
        and camo_card.cost == 3 \
        and camo_card.card_type == CardType.keep \
        and camo_card.effect == "If you lose [health], roll a die for each [health] you lost. " \
                                "Each [heart] reduces the loss by 1[heart]" \
        and camo_card.footnote == "(applicable to damages from both [attack] and Card effect)"


def test_card_parse_train():
    test_deck = parser.__deck_json_parser(mock_cards.mock_json_card_train)
    test_card = test_deck[0]
    assert test_card.name == "Commuter Train"
    assert test_card.cost == 4
    assert test_card.effect == "+ 2[Star]"
    assert test_card.footnote == ""
    assert test_card.card_type == CardType.discard


def test_card_parse_camo():
    test_deck = parser.__deck_json_parser(mock_cards.mock_json_card_camo)
    test_card = test_deck[0]
    assert test_card.name == "Camouflage"
    assert test_card.cost == 3
    assert test_card.effect == "If you lose [health], roll a die for each [health] you lost. " \
                               "Each [heart] reduces the loss by 1[heart]"
    assert test_card.footnote == "(applicable to damages from both [attack] and Card effect)"
    assert test_card.card_type == CardType.keep
    assert isinstance(test_card.cost, int)


def test_parse_bad_cards():
    test_deck = parser.__deck_json_parser(mock_cards.mock_json_bad_card_cost)
    assert len(test_deck) == 0

    test_deck = parser.__deck_json_parser(mock_cards.mock_json_bad_card_type)
    assert len(test_deck) == 0


test_parse_bad_cards()
