from game.cards.discard_card import DiscardCard


class Tanks(DiscardCard):
    def __init__(self):
        super().__init__("Tanks", 4, "+ 4[Star] - 3[Health]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(4)
        player_that_bought_the_card.update_health_by(-3)
