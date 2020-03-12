import datetime

from django.test import TestCase
from game.models import Game
from game.models import User
from game.models import Dice


class DiceModelTest(TestCase):

    @classmethod
    def setUp(cls):
        game = Game.objects.create(room_name='Room_1000',
                                   game_status='2',
                                   date_created=datetime.datetime.now())

        user = User.objects.create(game=game,
                                   monster_name='Godzilla',
                                   username='User1',
                                   date_created=datetime.datetime.now())

        Dice.objects.create(user=user,
                            re_rolls_left=1,
                            dice1='1',
                            dice2='2',
                            dice3='3',
                            dice4='a',
                            dice5='e',
                            dice6='1',
                            date_created=datetime.datetime.now())

    def test_user_content(self):
        dice = Dice.objects.get(dice2='2')
        expected_object_name = f'{dice.dice1}'
        self.assertEquals(expected_object_name, '1')
