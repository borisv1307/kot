from backend.src.game.newcards.discard_card import DiscardCard
from backend.src.game.newcards.new_card import NewCard


class ApartmentBuilding(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Apartment Building", 5, "+ 3[Star]")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(3)
