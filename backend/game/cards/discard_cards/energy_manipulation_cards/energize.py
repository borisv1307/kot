from game.cards.discard_card import DiscardCard


class Energize(DiscardCard):
    def __init__(self):
        super().__init__("Drop from High Altitude", 8, "+ 9[Energy]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_energy_by(9)
