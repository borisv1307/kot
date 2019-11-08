from game.newcards.discard_card import DiscardCard
from game.newcards.new_card import NewCard


class FireBlast(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Fire Blast", 3, "- 2[Energy]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_energy_cube_by(-2)
