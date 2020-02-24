from game.cards.keep_card import KeepCard


class Gourmet(KeepCard):
    def __init__(self):
        super().__init__("Gourmet", 4,
                         "When rolling [1][1][1] or more gain 2 extra [Star].")

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
