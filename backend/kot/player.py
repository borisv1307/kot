"""

"""


class Player:
    def __init__(self):

        self.victory_points = 0

        self.health = 10

        self.energy = 0

        self.power_cards = []

        self.location = ""

        return

    def heal(self, amount: int) -> None:

        # If it's the case that the player is not in Tokyo or Tokyo bay,
        if self.location == "":

            # We are going to heal up to a maximum of 10
            self.health = min(10, self.health + amount)
        return
