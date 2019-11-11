import game.dice.dice as dice


class DiceHandler:
    def __init__(self):
        self.dice_values = []
        self.re_rolls_left = 0

    def roll_initial(self, starting_dice_count, re_roll_count):
        self.dice_values = dice.roll_many(starting_dice_count)
        self.re_rolls_left = re_roll_count

    def re_roll_dice(self, indexes_of_dice_to_re_roll):
        if self.re_rolls_left <= 0:
            return

        if isinstance(indexes_of_dice_to_re_roll, int):
            indexes_of_dice_to_re_roll = [indexes_of_dice_to_re_roll]

        temp_values = self.dice_values.copy()
        for i in indexes_of_dice_to_re_roll:
            try:
                temp_values[i] = dice.roll()
            except IndexError:
                continue
        if self.dice_values != temp_values:
            self.dice_values = temp_values
            self.re_rolls_left -= 1

    def add_bonus_die(self, count_to_add=1):
        for _ in range(count_to_add):
            self.dice_values.append(dice.roll())

