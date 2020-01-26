from game.cards.keep_card import KeepCard


class EaterOfTheDead(KeepCard):
    def __init__(self):
        super().__init__("Eater of the Dead", 4,
                         "+ 3[Star] every time a monster's [Heart] goes to 0.")

    # TODO Determine when this special effect will occur
    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(3)
