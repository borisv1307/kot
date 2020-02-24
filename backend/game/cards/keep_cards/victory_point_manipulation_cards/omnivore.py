from game.cards.keep_card import KeepCard


class Omnivore(KeepCard):
    def __init__(self):
        super().__init__("Omnivore", 4,
                         "When you roll at least [1][2][3], gain 2[star]. You can use these dice in other combinations.")

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
