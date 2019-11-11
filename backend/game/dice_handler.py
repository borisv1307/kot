import game.dice.dice as dice


class DiceHandler:
    def __init__(self):
        self.dice_values = []
        self.re_rolls_left = 0

    def start_turn(self, starting_dice_count, re_roll_count):
        self.dice_values = dice.roll_many(starting_dice_count)
        self.re_rolls_left = re_roll_count

    def re_roll_dice(self, indexes_of_dice_to_re_roll):
        if self.re_rolls_left <= 0:
            return
        elif isinstance(indexes_of_dice_to_re_roll, int):
            try:
                self.dice_values[indexes_of_dice_to_re_roll] = dice.roll()
                self.re_rolls_left -= 1
            except IndexError:
                return
        elif isinstance(indexes_of_dice_to_re_roll, list) and \
                all(isinstance(item, int) for item in indexes_of_dice_to_re_roll):
            dice_modified = False
            for i in indexes_of_dice_to_re_roll:
                try:
                    self.dice_values[i] = dice.roll()
                    dice_modified = True
                except IndexError:
                    continue
            if dice_modified:
                self.re_rolls_left -= 1
        else:
            raise TypeError("re_roll_dice needs an int or list of ints of the indexes to re-roll")

    def add_bonus_die(self, count_to_add=1):
        for _ in range(count_to_add):
            self.dice_values.append(dice.roll())