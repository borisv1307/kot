from game.cards.keep_card import KeepCard
from game.values import locations


class Urbavore(KeepCard):
    def __init__(self):
        super().__init__("Urbavore", 4,
                         "Gain 1 extra [star] when beginning your turn in Tokyo. If you are in Tokyo and you roll at least one [attack] add [attack] to your roll")

    def special_effect(self, player_that_bought_the_card, other_players):
        if player_that_bought_the_card.location == locations.Locations.TOKYO:
            player_that_bought_the_card.update_victory_points_by(1)

    def attack_dice_special_effect(self, player_that_bought_the_card, attack_die_value):
        if player_that_bought_the_card.location == locations.Locations.TOKYO and attack_die_value >= 1:
            return attack_die_value + 1
        else:
            return attack_die_value
