import datetime

import pytest
from django.test import TestCase
from django.utils import timezone
from game.models import User



@pytest.mark.django_db
class test_PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        User.objects.create(monster_name='Godzilla',
                              username='User1',
                              password='Password1',
                              date_created=timezone.now())

    def test_user_content(self):
        player = User.objects.get(monster_name='Godzilla')
        expected_object_name = f'{player.username}'
        self.assertEquals(expected_object_name, 'User1')


