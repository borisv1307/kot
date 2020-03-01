from game.cards.discard_card import DiscardCard


class VastStorm(DiscardCard):
    def __init__(self):
        super().__init__("Vast Storm", 6, "+ 2[Star] - 1[Health]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
        player_that_bought_the_card.update_health_by(-1)
