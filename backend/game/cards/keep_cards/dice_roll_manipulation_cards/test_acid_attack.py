from game.cards.keep_cards.dice_roll_manipulation_cards.acid_attack import AcidAttack


def test_acid_attack_player_add_card(player):
    AcidAttack().immediate_effect(player, None)
    assert player.card_on_hand.get("Acid Attack") == "Add [attack] to your roll"


def test_acid_attack_costs_6_energy():
    assert AcidAttack().cost == 6
