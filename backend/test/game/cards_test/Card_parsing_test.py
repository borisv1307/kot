import pytest
import backend.src.game.cards.card_json_parser as Parser

mock_json_card_train = {
    "kot_cards": [
        {
            "name": "Commuter Train",
            "cost": 4,
            "card_type": "Discard",
            "effect": "+ 2[Star]",
            "footnote": ""
        }
    ]
}

mock_json_card_camo = {
    "kot_cards": [
        {
            "name": "Camouflage",
            "cost": 3,
            "card_type": "Keep",
            "effect": "If you lose [health], roll a die for each [health] you lost. "
                      "Each [heart] reduces the loss by 1[heart]",
            "footnote": "(applicable to damages from both [attack] and Card effect)"
        }
    ]
}

mock_json_bad_card_cost = {
    "kot_cards": [
        {
            "name": "Commuter Train",
            "cost": "99",
            "card_type": "Discard",
            "effect": "+ 2[Star]",
            "footnote": ""
        }
    ]
}

mock_json_bad_card_type = {
    "kot_cards": [
        {
            "name": "Commuter Train",
            "cost": "99",
            "card_type": "Discood",
            "effect": "+ 2[Star]",
            "footnote": ""
        }
    ]
}

mock_json_2_cards = {
    "kot_cards": [
        {
            "name": "Commuter Train",
            "cost": 4,
            "card_type": "Discard",
            "effect": "+ 2[Star]",
            "footnote": ""
        },
        {
            "name": "Camouflage",
            "cost": 3,
            "card_type": "Keep",
            "effect": "If you lose [health], roll a die for each [health] you lost. "
                      "Each [heart] reduces the loss by 1[heart]",
            "footnote": "(applicable to damages from both [attack] and Card effect)"
        }
    ]
}


def test_deck_multiple_cards():
    test_deck = Parser.__deck_json_parser(mock_json_2_cards)
    assert len(test_deck) == 2

    commuter_card = test_deck[0]
    assert commuter_card.name == "Commuter Train" \
        and commuter_card.cost == 4 \
        and commuter_card.card_type == Parser.CardType.discard \
        and commuter_card.effect == "+ 2[Star]" \
        and commuter_card.footnote == ""

    camo_card = test_deck[1]
    assert camo_card.name == "Camouflage" \
        and camo_card.cost == 3 \
        and camo_card.card_type == Parser.CardType.keep \
        and camo_card.effect == "If you lose [health], roll a die for each [health] you lost. " \
                                "Each [heart] reduces the loss by 1[heart]" \
        and camo_card.footnote == "(applicable to damages from both [attack] and Card effect)"


def test_card_parse_train():
    test_deck = Parser.__deck_json_parser(mock_json_card_train)
    test_card = test_deck[0]
    assert test_card.name == "Commuter Train"
    assert test_card.cost == 4
    assert test_card.effect == "+ 2[Star]"
    assert test_card.footnote == ""
    assert test_card.card_type == Parser.CardType.discard


def test_card_parse_camo():
    test_deck = Parser.__deck_json_parser(mock_json_card_camo)
    test_card = test_deck[0]
    assert test_card.name == "Camouflage"
    assert test_card.cost == 3
    assert test_card.effect == "If you lose [health], roll a die for each [health] you lost. " \
                               "Each [heart] reduces the loss by 1[heart]"
    assert test_card.footnote == "(applicable to damages from both [attack] and Card effect)"
    assert test_card.card_type == Parser.CardType.keep
    assert isinstance(test_card.cost, int)


def test_parse_bad_cards():
    test_deck = Parser.__deck_json_parser(mock_json_bad_card_cost)
    assert len(test_deck) == 0

    test_deck = Parser.__deck_json_parser(mock_json_bad_card_type)
    assert len(test_deck) == 0


test_parse_bad_cards()