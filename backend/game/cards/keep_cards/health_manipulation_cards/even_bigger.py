from game.cards.card import Card
from game.cards.keep_card import KeepCard


class EvenBigger(KeepCard):
    def __init__(self):
        Card.__init__(self, "Even Bigger", 4,
                      "+2[health] when you buy this card.maximum [health] increased to 12 as long as you own this card",
                      "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        card = EvenBigger()
        player_that_bought_the_card.add_card(card)

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.maximum_health = 12
        player_that_bought_the_card.update_health_by(2)
