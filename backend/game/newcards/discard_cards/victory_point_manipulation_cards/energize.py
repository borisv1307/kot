from game.newcards.discard_card import DiscardCard
from game.newcards.new_card import NewCard


class Energize(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Drop from High Altitude", 8, "+ 9[Energy]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_energy_cube_by(9)
