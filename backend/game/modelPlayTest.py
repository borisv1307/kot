import datetime

from django.test import TestCase

from game.models import Dice
from game.models import Game
from game.models import Play
from game.models import User


class PlayModelTest(TestCase):

    @classmethod
    def setUp(cls):
        game = Game.objects.create(room_name='Room_1000',
                                   game_status='2',
                                   date_created=datetime.datetime.now())

        user = User.objects.create(game=game,
                                   monster_name='Godzilla',
                                   username='User1',
                                   date_created=datetime.datetime.now())

        Play.objects.create(user=user,
                            card1_swept='Test1',
                            card1_swept_type='K',
                            card2_swept='Test2',
                            card2_swept_type='D',
                            card3_swept='Test3',
                            card3_swept_type='D',
                            card_purchased='Card1',
                            card_purchased_type='K',
                            card_used='Card2',
                            location='T',
                            victory_points='20',
                            energy_cubes='30',
                            health_points='40',
                            date_created=datetime.datetime.now())

    def test_user_content(self):
        play = Play.objects.get(card1_swept='Test1')
        expected_object_name = f'{play.location}'
        self.assertEquals(expected_object_name, 'T')
