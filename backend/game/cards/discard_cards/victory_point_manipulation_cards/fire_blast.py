from game.cards.discard_card import DiscardCard
from game.cards.card import Card


class FireBlast(DiscardCard):
    def __init__(self):
        Card.__init__(self, "Fire Blast", 3, "All other monsters - 2[health]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        for other_player in other_players:
            other_player.update_energy_cube_by(-2)
