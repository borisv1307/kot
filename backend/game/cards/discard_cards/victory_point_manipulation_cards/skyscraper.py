from game.cards.discard_card import DiscardCard


class Skyscraper(DiscardCard):
    def __init__(self):
        super().__init__("Skyscraper", 6, "+ 4[Star]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(4)
