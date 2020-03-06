import game.turn_actions.player_movement as player_movement
from game.cards.discard_card import DiscardCard
from game.values.locations import Locations


class DropFromHighAltitude(DiscardCard):
    """
        All logic for selecting who is yielding must occur prior to invoking this card
    """

    def __init__(self):
        super().__init__("Drop from High Altitude", 5,
                         "+ 2[Star] and take control of Tokyo if you don't already control it",
                         "(player choose to take control either City & Bay if both are occupied)")

    def immediate_effect(self, player_that_bought_the_card, yielding_player=None):
        player_that_bought_the_card.update_victory_points_by(2)
        if yielding_player:
            if player_that_bought_the_card.location == Locations.OUTSIDE and yielding_player.location != Locations.OUTSIDE:
                player_movement.yield_tokyo(yielding_player, player_that_bought_the_card)
