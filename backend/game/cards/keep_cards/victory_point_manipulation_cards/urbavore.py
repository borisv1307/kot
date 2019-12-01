from game.cards.card import Card
from game.cards.keep_card import KeepCard
from game.values import locations


class Urbavore(KeepCard):
    def __init__(self):
        Card.__init__(self, "Urbavore", 4,
                      "gain 1 extra [star] when beginning your turn in Tokyo. If your are in Tokyo and you roll at least one [attack] add [attack] to your roll",
                      "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        card = Urbavore()
        player_that_bought_the_card.add_card(card)

    def special_effect(self, player_that_bought_the_card, other_players):
        if player_that_bought_the_card.location == locations.Locations.TOKYO:
            player_that_bought_the_card.update_victory_points_by(1)

# TODO Turn related logic for attack
