from game.cards.keep_card import KeepCard


class Regeneration(KeepCard):
    def __init__(self):
        super().__init__("Regeneration", 4,
                         "When you gain [health], gain 1 extra [health]")

    def special_effect(self, player_that_bought_the_card, health):
        if health >= 1:
            health += 1
        return health
