from game.cards.discard_card import DiscardCard


class Frenzy(DiscardCard):
    def __init__(self):
        super().__init__("Frenzy", 7,
                         "Take another turn after this one", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.gets_bonus_turn = True
