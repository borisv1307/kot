from game.cards.keep_card import KeepCard


class RootingForTheUnderdog(KeepCard):
    def __init__(self):
        super().__init__("Rooting for the Underdog", 3,
                         "At the end of a turn if you have the fewest [Star] gain 1 [Star].",
                         "No [star] if tied fewest; at the end of your turn")

    def special_effect(self, player_that_bought_the_card, other_players):
        min_victory_points = min(
            [other_player.victory_points for other_player in other_players])
        if player_that_bought_the_card.victory_points < min_victory_points:
            player_that_bought_the_card.update_victory_points_by(1)
