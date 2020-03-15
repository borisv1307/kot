from game.cards.keep_card import KeepCard


class AlphaMonster(KeepCard):
    def __init__(self):
        super().__init__("Alpha Monster", 5,
                         "Gain 1[Star] when you Roll at least one [attack].")

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(1)
