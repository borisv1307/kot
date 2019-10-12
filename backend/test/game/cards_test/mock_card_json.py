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
