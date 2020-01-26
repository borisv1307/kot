from game.cards.card import Card
from game.cards.keep_card import KeepCard


class ItHasAChild(KeepCard):
    def __init__(self):
        super().__init__("It Has a Child", 7,
                         "If you reach 0[health] discard all your cards and lose all you [star]. Gain 10[health] and continue playing outside Tokyo.")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        card = ItHasAChild()
        player_that_bought_the_card.add_card(card)

    def special_effect(self, player_that_bought_the_card, other_players):
        if player_that_bought_the_card.current_health <= 0:
            self._discard_all_cards(player_that_bought_the_card, other_players)
            player_that_bought_the_card.lose_all_stars()
            player_that_bought_the_card.leave_tokyo()
            player_that_bought_the_card.current_health = 10

    def _discard_all_cards(self, player_that_bought_the_card, other_players):
        for cards in player_that_bought_the_card.cards:
            cards.discard_effect(player_that_bought_the_card, other_players)
