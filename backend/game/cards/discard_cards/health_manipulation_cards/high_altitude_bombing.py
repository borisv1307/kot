from game.cards.discard_card import DiscardCard
from game.cards.card import Card


class HighAltitudeBombing(DiscardCard):
    def __init__(self):
        Card.__init__(self, "High Altitude Bombing", 4, "All monsters (including you) - 3[health]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_health_by(-3)
        for other_player in other_players:
            other_player.update_health_by(-3)
