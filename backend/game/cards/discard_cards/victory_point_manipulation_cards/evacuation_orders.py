from game.cards.discard_card import DiscardCard
from game.cards.new_card import NewCard


class EvacuationOrders(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Evacuation Orders", 7,
                         "All other monsters lose 5[Star].")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        for other_player in other_players:
            other_player.update_victory_points_by(-5)
