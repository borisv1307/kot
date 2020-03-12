import datetime

from django.test import TestCase
from game.models import Game


class GameModelTest(TestCase):

    @classmethod
    def setUp(cls):
        Game.objects.create(room_name='Room_1000',
                            game_status='2',
                            date_created=datetime.datetime.now())

    def test_user_content(self):
        game = Game.objects.get(room_name='Room_1000')
        expected_object_name = f'{game.game_status}'
        self.assertEquals(expected_object_name, '2')
