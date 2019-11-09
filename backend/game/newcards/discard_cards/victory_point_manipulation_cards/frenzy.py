from game.newcards.discard_card import DiscardCard
from game.newcards.new_card import NewCard


class Frenzy(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Frenzy", 7, "Take another turn after this one", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(0)
        # add detail for next turn
