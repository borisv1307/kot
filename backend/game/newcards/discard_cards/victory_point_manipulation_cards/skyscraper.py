from game.newcards.discard_card import DiscardCard
from game.newcards.new_card import NewCard


class Skyscraper(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Skyscraper", 6, "+ 4[Star]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(4)