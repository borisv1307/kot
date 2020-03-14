from game.cards.keep_card import KeepCard


class ArmorPlating(KeepCard):
    def __init__(self):
        super().__init__("Armor Plating", 4,
                         "Do not lose 1[health] when you lose exactly 1[health]",
                         "Damages from [attack] and each Card effect are considered separatelys")

    def special_effect(self, player_that_bought_the_card, health):
        if health == -1:
            health = 0
        return health
