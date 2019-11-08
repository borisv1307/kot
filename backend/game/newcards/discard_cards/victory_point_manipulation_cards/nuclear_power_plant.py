from game.newcards.discard_card import DiscardCard
from game.newcards.new_card import NewCard


class NuclearPowerPlant(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Nuclear Power Plant", 6, "+ 2[Star] + 3[Health]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
        player_that_bought_the_card.update_health_by(3)
