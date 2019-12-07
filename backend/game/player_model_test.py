import datetime

from django.test import TestCase

from .models import User


class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        User.objects.create(monster_name='Godzilla',
                              username='User1',
                              password='Password1',
                              date_created=datetime.datetime.now())

    def test_user_content(self):
        player = User.objects.get(monster_name='Godzilla')
        expected_object_name = f'{player.monster_name}'
        self.assertEquals(expected_object_name, 'Godzilla')
