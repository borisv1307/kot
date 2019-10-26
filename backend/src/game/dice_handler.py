import backend.src.game.dice as dice
import backend.src.game.constants as constants


class DiceHandler:
    dice_values = []
    re_rolls_left = constants.DEFAULT_RE_ROLL_COUNT

    def start_turn(self):
        self.dice_values = dice.roll_many(constants.DEFAULT_DICE_COUNT)
        self.re_rolls_left = constants.DEFAULT_RE_ROLL_COUNT

    def re_roll_dice(self, indexes_of_dice_to_re_roll):
        if self.re_rolls_left <= 0:
            return

        if type(indexes_of_dice_to_re_roll) == int:
            self.dice_values[indexes_of_dice_to_re_roll] = dice.roll()

        elif type(indexes_of_dice_to_re_roll) == list:
            for val in indexes_of_dice_to_re_roll:
                self.dice_values[val] = dice.roll()
            self.re_rolls_left -= 1

    def add_bonus_die(self):
        self.dice_values.append(dice.roll())
