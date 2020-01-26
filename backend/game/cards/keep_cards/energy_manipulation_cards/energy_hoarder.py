from game.cards.card import Card
from game.cards.keep_card import KeepCard
from game.values import constants


class EnergyHoarder(KeepCard):
    def __init__(self):
        Card.__init__(self, "Energy Hoarder", 3,
                      "You gain 1[Star] for every 6[Energy] you have at the end of your turn.", "")

    def special_effect(self, player_that_bought_the_card, other_players):
        num_stars = player_that_bought_the_card.energy // constants.ENERGY_HOARDER_DIVIDER
        player_that_bought_the_card.update_victory_points_by(num_stars)
