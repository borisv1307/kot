"""
This is a class that keeps the state of a given player for the game King of
Tokyo.




Locations at the player can be:
    - (blank): Denotes that the player is not on the game board.
    - Tokyo: The player is in Tokyo
    - Tokyo Bay: The player is in the alternative Tokyo location for 5+ players
"""


class Player:
    def __init__(self):

        self.victory_points = 0

        # There's one card that gives a player a max health of 12.
        # Because of this, we may want to consider adding a max_health var
        self.health = 10

        # Energy cubes are the resource that is used to purchase the upgrades
        # that are given by the upgrade cards that a player has.

        # Alternatively, two energy can be spent to discard and receive three
        # new cards.
        self.energy = 0

        # This is a list of the cards that a player gets during the game.
        self.power_cards = []

        # The player starts the game not being in Tokyo or Tokyo Bay. An empty
        # string denotes that they are not in either of these places.
        self.location = ""

        return

    def heal(self, amount: int) -> None:

        # If it's the case that the player is not in Tokyo or Tokyo bay,
        if self.location == "":

            # We are going to heal up to a maximum of 10
            self.health = min(10, self.health + amount)
        return

    def yield_tokyo(self) -> None:
        self.location = ""

    def discard(self):

        discarded_cards = self.power_cards

        self.power_cards = []

        return discarded_cards
