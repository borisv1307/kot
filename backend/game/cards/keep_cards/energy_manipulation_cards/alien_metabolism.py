from game.cards.keep_card import KeepCard


class AlienMetabolism(KeepCard):
    def __init__(self):
        super().__init__("Alien Metabolism", 3,
                         "Buying Power cards costs you 1 less [Energy].")

    def special_effect(self, player_that_bought_the_card, other_players):
        pass
