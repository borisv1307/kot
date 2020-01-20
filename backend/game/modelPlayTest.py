
import datetime

from django.test import TestCase

from game.models import Dice
from game.models import Game
from game.models import Play
from game.models import User


class PlayModelTest(TestCase):

    @classmethod
    def setUp(cls):
        user = User.objects.create(monster_name='Godzilla',
                                   username='User1',
                                   password='Password1',
                                   date_created=datetime.datetime.now())

        game = Game.objects.create(user=user,
                                   is_winner='Y',
                                   num_players='10',
                                   player_position='1',
                                   date_created=datetime.datetime.now(),
                                   date_modified=datetime.datetime.now())

        dice = Dice.objects.create(user=user,
                                   dice1='1',
                                   dice1_selected='Y',
                                   dice2='1',
                                   dice2_selected='Y',
                                   dice3='1',
                                   dice3_selected='Y',
                                   dice4='1',
                                   dice4_selected='Y',
                                   dice5='1',
                                   dice5_selected='Y',
                                   dice6='1',
                                   dice6_selected='Y',
                                   date_created=datetime.datetime.now())

        Play.objects.create(user=user,
                            game=game,
                            dice=dice,
                            card_purchased='Card1',
                            card_used='Card2',
                            location='T',
                            victory_points='20',
                            energy_cube='30',
                            life_points='40',
                            date_created=datetime.datetime.now())

    def test_user_content(self):
        play = Play.objects.get(user=1)
        expected_object_name = f'{play.location}'
        self.assertEquals(expected_object_name, 'T')

