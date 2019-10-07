"""
This is a class that keeps the state of a given player for the game King of
Tokyo.
"""


class Player:
    """
    Locations at the player can be:
    - (blank): Denotes that the player is not on the game board.
    - Tokyo: The player is in Tokyo
    - Tokyo Bay: The player is in the alternative Tokyo location for 5+ players
    """
    def __init__(self):

        # These are the points that the player earns throughout the game.
        # Once they have gained a total of 20 (while keeping their health above
        # 0), they are considered to have won the game.
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

        if self.location == "":
            raise Exception("Player was not in Tokyo!")

        self.location = ""

        return

    def discard(self):

        if self.energy < 2:
            raise Exception("Player did not have enough energy!")

        self.energy -= 2

        discarded_cards = self.power_cards

        # I was initially concerned that this would cause the discarded_cards
        # to also be zeroed out, but I tested it and this is fine. The other
        # keeps the pointer to the original while power_cards is set.
        self.power_cards = []

        return discarded_cards
