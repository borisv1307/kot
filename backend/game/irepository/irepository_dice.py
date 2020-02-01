import datetime

from game.models import User
from game.models import Dice
from game.player.player import Player
from game.dice_handler import DiceHandler


class IRepositoryDice:

    def __init__(self):
        self.dice = None

    def save_dice_db(self, player: Player, dice: DiceHandler):
        if dice.re_rolls_left > 0:
            re_roll = True
        self.dice = Dice(user=User.objects.get(monster_name=player.monster_name),
                         dice1=dice.dice_values[0],
                         dice1_selected='Y',
                         dice2=dice.dice_values[1],
                         dice2_selected='Y',
                         dice3=dice.dice_values[2],
                         dice3_selected='Y',
                         dice4=dice.dice_values[3],
                         dice4_selected='Y',
                         dice5=dice.dice_values[4],
                         dice5_selected='Y',
                         dice6=dice.dice_values[5],
                         dice6_selected='Y',
                         date_created=datetime.datetime.now(),
                         allowReroll=re_roll)
        self.dice.save()
        return self.dice

    def get_dice_db(self, player: Player):
        self.dice = Dice.objects.get(user=User.objects.get(monster_name=player.monster_name).id)
        return self.dice

    def update_dice_db(self, player: Player, dice: DiceHandler):
        self.dice = Dice.objects.get(user=User.objects.get(monster_name=player.monster_name).id)
        if dice.re_rolls_left > 0:
            re_roll = True
        self.dice.dice1 = dice.dice_values[0]
        self.dice.dice2 = dice.dice_values[1]
        self.dice.dice3 = dice.dice_values[2]
        self.dice.dice4 = dice.dice_values[3]
        self.dice.dice5 = dice.dice_values[4]
        self.dice.dice6 = dice.dice_values[5]
        self.dice.allowReroll = re_roll
        self.dice.save()
        return self.dice

    def update_die_db(self, player: Player, dice_number, dice_value, re_roll):
        self.dice = Dice.objects.get(user=User.objects.get(monster_name=player.monster_name).id)
        if dice_number == 1:
            self.dice.dice1 = dice_value
        elif dice_number == 2:
            self.dice.dice2 = dice_value
        elif dice_number == 3:
            self.dice.dice3 = dice_value
        elif dice_number == 4:
            self.dice.dice4 = dice_value
        elif dice_number == 5:
            self.dice.dice5 = dice_value
        elif dice_number == 6:
            self.dice.dice6 = dice_value
        self.dice.allowReroll = re_roll
        self.dice.save()
        return self.dice

    def delete_dice_db(self, player: Player):
        self.dice = Dice.objects.get(user=User.objects.get(monster_name=player.monster_name).id)
        self.dice.delete()
        return None
