from game.cards.discard_card import DiscardCard
from game.cards.card import Card


class CommuterTrain(DiscardCard):
    def __init__(self):
        Card.__init__(self, "Commuter Train", 4, "+ 2[Star]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
