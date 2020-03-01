from game.cards.keep_card import KeepCard


class NovaBreath(KeepCard):
    def __init__(self):
        super().__init__("Nova Breath", 7,
                         "Your [attack] Smash all other monsters")

    def special_effect(self, player_that_bought_the_card, other_players):
        pass
