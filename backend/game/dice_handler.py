import game.dice.dice as dice


class DiceHandler:
    def __init__(self):
        self.dice_values = []
        self.re_rolls_left = 0

    def start_turn(self, starting_dice_count, re_roll_count):
        self.dice_values = dice.roll_many(starting_dice_count)
        self.re_rolls_left = re_roll_count

    def re_roll_dice(self, indexes_of_dice_to_re_roll):
        if self.re_rolls_left > 0:
            try:
                for val in indexes_of_dice_to_re_roll:
                    self.dice_values[val] = dice.roll()
                self.re_rolls_left -= 1
            except IndexError:
                raise IndexError("Re-roll index outside of dice_values range")
            except TypeError:
                raise TypeError("Re-roll index must be passed as list of ints")

    def add_bonus_die(self):
        self.dice_values.append(dice.roll())
