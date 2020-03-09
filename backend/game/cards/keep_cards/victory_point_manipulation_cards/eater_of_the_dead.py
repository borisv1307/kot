from game.cards.keep_card import KeepCard


class EaterOfTheDead(KeepCard):
    victory_points_reward_value = 3

    def __init__(self):
        super().__init__("Eater of the Dead", 4,
                         "+ 3[Star] every time a monster's [Heart] goes to 0.")

    def special_effect(self, player_that_bought_the_card, other_players=None):
        player_that_bought_the_card.update_victory_points_by(self.victory_points_reward_value)
