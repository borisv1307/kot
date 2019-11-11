from game.cards.card import Card
from game.cards.discard_card import DiscardCard
from game.values.locations import Locations


class DropFromHighAltitude(DiscardCard):
    def __init__(self):
        Card.__init__(self, "Drop from High Altitude", 5, "+ 2[Star] and take control of Tokyo if you don't already "
                                                          "control it", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
        for other_player in other_players:
            if other_player.location == Locations.TOKYO:
                other_player.leave_tokyo()
        player_that_bought_the_card.move_to_tokyo()
