from game.cards.keep_card import KeepCard


class WereOnlyMakingItStronger(KeepCard):
    def __init__(self):
        super().__init__("We're Only Making It Stronger", 3,
                         "When you lose 2[health] or more gain 1[energy].")

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_energy_by(1)
