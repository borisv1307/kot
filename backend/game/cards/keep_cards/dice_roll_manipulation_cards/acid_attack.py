from game.cards.card import Card
from game.cards.keep_card import KeepCard


class AcidAttack(KeepCard):
    def __init__(self):
        Card.__init__(self, "Acid Attack", 6, "Add [attack] to your roll", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        Card.name = "Acid Attack"
        Card.cost = 6
        Card.footnote = ""
        Card.effect = "Add [attack] to your roll"
        player_that_bought_the_card.add_keep_card(Card)
