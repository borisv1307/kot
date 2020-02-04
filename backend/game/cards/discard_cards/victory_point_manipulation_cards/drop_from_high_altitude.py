from game.cards.discard_card import DiscardCard
from game.values.locations import Locations
import game.turn_actions.player_movement as player_movement


class DropFromHighAltitude(DiscardCard):
    def __init__(self):
        super().__init__("Drop from High Altitude", 5,
                         "+ 2[Star] and take control of Tokyo if you don't already control it")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
        player_movement.move_players_out_of_tokyo(other_players)
        player_that_bought_the_card.move_to_tokyo()
