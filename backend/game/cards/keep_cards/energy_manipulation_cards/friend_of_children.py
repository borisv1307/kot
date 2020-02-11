from game.cards.keep_card import KeepCard


class FriendOfChildren(KeepCard):
    def __init__(self):
        super().__init__("Friend of Children", 3,
                         "When you gain any [Energy] gain 1 extra [Energy].")

    def special_effect(self, player_that_bought_the_card, other_players):
        pass

    def add_extra_energy(change_integer):
        if change_integer >= 1:
            change_integer += 1
        return change_integer
