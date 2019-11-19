from game.cards.keep_cards.victory_points_manipulation_cards.eater_of_the_dead import EaterOfTheDead


def test_eater_of_the_dead(player):
    # This will add the card to the player's hand
    EaterOfTheDead().immediate_effect(player, None)
    # Need to assert whether the player currently holds the eater of the dead card
