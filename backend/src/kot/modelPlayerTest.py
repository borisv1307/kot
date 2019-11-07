import datetime

from django.test import TestCase

from .models import Player


class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        Player.objects.create(monster_name='Godzilla',
                              username='User1',
                              password='Password1',
                              date_created=datetime.datetime.now())

    def test_user_content(self):
        player = Player.objects.get(monster_name='Godzilla')
        expected_object_name = f'{player.monster_name}'
        self.assertEquals(expected_object_name, 'Godzilla')
