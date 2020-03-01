from game.cards.discard_card import DiscardCard


class JetFighters(DiscardCard):
    def __init__(self):
        super().__init__("Jet Fighters", 5, "+ 5[star] - 4[health]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(5)
        player_that_bought_the_card.update_health_by(-4)
