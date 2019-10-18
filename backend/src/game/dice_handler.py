import backend.src.game.dice as dice
import backend.src.game.constants as constants


class DiceHandler(object):
    dice_values = list()
    __re_rolls_left = constants.DEFAULT_REROLL_COUNT

    def start_turn(self):
        self.dice_values = dice.roll_many(constants.DEFAULT_DICE_COUNT)
        self.__re_rolls_left = constants.DEFAULT_REROLL_COUNT

    def re_roll_dice(self, indexes_of_dice_to_re_roll):
        if self.__re_rolls_left > 0:
            if type(indexes_of_dice_to_re_roll) == int:
                self.dice_values[indexes_of_dice_to_re_roll] = dice.roll()

            elif type(indexes_of_dice_to_re_roll) == list:
                for val in indexes_of_dice_to_re_roll:
                    self.dice_values[val] = dice.roll()
                self.__re_rolls_left -= 1

    def add_bonus_die(self):
        self.dice_values.append(dice.roll())

