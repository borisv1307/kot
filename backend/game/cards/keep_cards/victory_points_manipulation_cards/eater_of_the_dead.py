from game.cards.keep_card import KeepCard
from game.cards.card import Card
from game.values import constants


class EaterOfTheDead(KeepCard):
    def __init__(self):
        Card.__init__(self, "Eater of the Dead", 4, "Gain 3[Star] every time a monster's [Heart] goes to 0.")

    def special_effect(self, player_that_bought_the_card, other_players):
        for other_player in other_players:
            if other_player.current_health == constants.DEATH_HIT_POINT:
                player_that_bought_the_card.update_victory_points_by(3)




