from game.models import Dice
from game.player.player import Player
from game.models import User
from django.utils import timezone


def dice_roll_to_db(dice: [Dice], indexes_to_re_roll: [int]):
    dummy_user = User.objects.create(monster_name='Godzilla',
                               username='User1',
                               password='Password1',
                               date_created=timezone.now())

    Dice.objects.create(user=dummy_user,
                        dice1=dice[0],
                        dice1_selected='Y',
                        dice2=dice[1],
                        dice2_selected='Y',
                        dice3=dice[2],
                        dice3_selected='Y',
                        dice4=dice[3],
                        dice4_selected='Y',
                        dice5=dice[4],
                        dice5_selected='Y',
                        dice6=dice[5],
                        dice6_selected='Y',
                        date_created=timezone.now())
