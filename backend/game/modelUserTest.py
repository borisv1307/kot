import datetime

from django.test import TestCase

from game.models import Game
from game.models import User


class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        game = Game.objects.create(room_name='Room_1000',
                                   game_status='2',
                                   date_created=datetime.datetime.now())

        User.objects.create(game=game,
                            monster_name='Godzilla',
                            username='User1',
                            date_created=datetime.datetime.now())

    def test_user_content(self):
        user = User.objects.get(monster_name='Godzilla')
        expected_object_name = f'{user.monster_name}'
        self.assertEquals(expected_object_name, 'Godzilla')
