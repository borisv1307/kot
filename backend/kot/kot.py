"""



Game events:
    Player turn:
        Start of turn
        Dice resolution
        Card buying (Optional)
        End of turn

    Player death (reaching 0 life)
    Player win (reaching 20 victory points while life > 0)
    Player damage (in the event of an attack, not including damage from cards)
"""

import dice


class KingOfTokyo:

    def __init__(self, players):

        self.players = players

        self.current_player = 0

        return

    def decide_who_goes_first(self, players):
        # According to the rules, each player rolls six dice. The player that
        # gets the most attach dice goes first.

        # While this was not stated, I am guessing that, in the event of a tie,
        # then those that tied should re-roll (could be more than two).
        dice_rolls = [[dice.roll() for _ in range(6)] for p in players]

        # We will set the next player's index to the current highest roll
        next_player_index = dice_rolls.index(sorted(dice_rolls)[0])

        # If it's the case that the two highest rolls are the same, we should
        # grab those players and re-call this method with only them.
        # For now, even if there's a tie, just go on.
        # self.decide_who_goes_first(players)

        # I was worried for a quick minute that we might get down to a single
        # player rolling against themselves, but that will never be the case
        # because it will get down to two players, have them roll, and, if it's
        # the same, they will re-roll against each other otherwise one wins.

        # TODO: Consider returning the dice rolls as well for the players
        # potentially this could be kept as state within the player or game?
        # We could keep the person's last roll or all of their rolls so we can
        # give a historical record of the game?
        return next_player_index

    def next_turn(self, player_index):
        return
