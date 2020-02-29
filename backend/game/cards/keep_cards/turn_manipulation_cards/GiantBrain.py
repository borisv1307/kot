from game.cards.keep_card import KeepCard


class GiantBrain(KeepCard):
    def __init__(self):
        super().__init__("Giant Brain", 5, "You have 1 extra die roll each turn")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        pass

    def discard_effect(self, player_that_bought_the_card, other_players):
        pass

    def special_effect(self, player_that_bought_the_card, other_players):
        pass
