from game.cards.keep_card import KeepCard


class CompleteDestruction(KeepCard):
    def __init__(self):
        super().__init__("Complete Destruction", 3,
                         "If you roll [1][2][3][Heart][Attack][Energy] gain 9[Star] in addition to the regular results.")

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(9)
