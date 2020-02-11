from game.cards.discard_card import DiscardCard


class NationalGuard(DiscardCard):
    def __init__(self):
        super().__init__("National Guard", 3, "+ 2[Star] -2 [Health]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
        player_that_bought_the_card.update_health_by(-2)
