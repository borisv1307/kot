import datetime
from game.models import User
from game.models import Dice
from game.models import Game
from game.player.player import Player


class IRepositoryDice:

    def __init__(self):
        self.dice = None

    def save_dice(self, player: Player, room, dice1, dice2, dice3, dice4, dice5, dice6, dice7, dice8, roll):
        self.dice = Dice(
            user=User.objects.get(monster_name=player.monster_name, game=Game.objects.get(room_name=room)),
            roll_number=roll,
            dice1=dice1,
            dice1_selected='Y',
            dice2=dice2,
            dice2_selected='Y',
            dice3=dice3,
            dice3_selected='Y',
            dice4=dice4,
            dice4_selected='Y',
            dice5=dice5,
            dice5_selected='Y',
            dice6=dice6,
            dice6_selected='Y',
            dice7=dice7,
            dice7_selected='N',
            dice8=dice8,
            dice8_selected='N',
            date_created=datetime.datetime.now())
        self.dice.save()
        return self.dice.id

    def get_dice_by_id(self, dice_id):
        self.dice = Dice.objects.get(id=dice_id)
        return self.dice

    def get_all_dice_by_player_and_room(self, player: Player, room):
        self.dice = Dice.objects.get(user=User.objects.get(monster_name=player.monster_name,
                                                              game=Game.objects.get(room_name=room)).id)
        return self.dice

    def update_dice_by_id(self, dice_id, dice1, dice2, dice3, dice4, dice5, dice6, dice7, dice8, roll):
        self.dice = Dice.objects.get(id=dice_id)
        self.dice.roll_number = roll
        self.dice.dice1 = dice1
        self.dice.dice2 = dice2
        self.dice.dice3 = dice3
        self.dice.dice4 = dice4
        self.dice.dice5 = dice5
        self.dice.dice6 = dice6
        self.dice.dice7 = dice7
        self.dice.dice8 = dice8
        self.dice.save()
        return self.dice

    def update_die_by_id(self, dice_id, dice_number, dice_value, roll):
        self.dice = Dice.objects.get(id=dice_id)
        self.dice.roll_number = roll
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
        elif dice_number == 7:
            self.dice.dice7 = dice_value
        elif dice_number == 8:
            self.dice.dice8 = dice_value
        self.dice.save()
        return self.dice

    def delete_dice_by_id(self, dice_id):
        self.dice = Dice.objects.get(id=dice_id)
        self.dice.delete()
        return None
