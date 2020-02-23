from game.cards.keep_card import KeepCard
from game.values import constants


class DedicatedNewsTeam(KeepCard):
    def __init__(self):
        super().__init__("Dedicated News Team", 3,
                         "Gain 1[Star] whenever you buy a Power card.")

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(1)
