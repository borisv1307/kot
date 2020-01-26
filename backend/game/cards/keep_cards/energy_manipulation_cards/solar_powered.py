from game.cards.keep_card import KeepCard


class SolarPowered(KeepCard):
    def __init__(self):
        super().__init__("Solar Powered", 4, "At the end of your turn gain 1[Energy] if you have no [Energy].")

    def special_effect(self, player_that_bought_the_card, other_players):
        if player_that_bought_the_card.energy == 0:
            player_that_bought_the_card.update_energy_by(1)
