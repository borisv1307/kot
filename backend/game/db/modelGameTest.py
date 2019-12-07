import datetime

from django.test import TestCase

from game.models import Game
from game.models import User



class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        player = User.objects.create(monster_name='Godzilla',
                                       username='User1',
                                       password='Password1',
                                       date_created=datetime.datetime.now())

        Game.objects.create(user=player,
                            is_winner='Y',
                            num_players='10',
                            player_position='1',
                            date_created=datetime.datetime.now(),
                            date_modified=datetime.datetime.now())

    def test_user_content(self):
        game = Game.objects.get(user=1)
        expected_object_name = f'{game.is_winner}'
        self.assertEquals(expected_object_name, 'Y')
