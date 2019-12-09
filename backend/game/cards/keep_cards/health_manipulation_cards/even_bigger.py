from game.cards.card import Card
from game.cards.keep_card import KeepCard


class EvenBigger(KeepCard):
    def __init__(self):
        super(KeepCard, self).__init__("Even Bigger", 4,
                                         "Your maximum [Heart] is increased by 2. Gain 2[Heart] when you get this card",
                                         "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.add_card(self)
        EvenBigger().special_effect(player_that_bought_the_card, None)

    def discard_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.remove_card(self)
        player_that_bought_the_card.update_max_health_by(-2)

    def special_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_max_health_by(2)
        player_that_bought_the_card.update_health_by(2)
