from game.cards.card import Card
from game.cards.discard_card import DiscardCard


class Heal(DiscardCard):
    def __init__(self):
        Card.__init__(self, "Heal", 3, "+ 2[Health]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_health_by(2)
