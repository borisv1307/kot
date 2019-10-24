# import pytest
from django.test import TestCase

from .models import Player


class UserModelTest(TestCase):

    # @pytest.fixture()
    # @pytest.mark.django_db
    @classmethod
    def setUpUser(cls):
        # super(UserModelTest, cls).setUpClass()
        Player.objects.create(monster_name='Godzilla')
        Player.objects.create(username='User1')
        Player.objects.create(password='Password1')
        # User.objects.create(date_created=datetime.datetime.now())
        # User.save()

    def test_user_content(self):
        player = Player.objects.filter(monster_name='Godzilla')
        expected_object_name = f'{player.monster_name}'
        self.assertEquals(expected_object_name, "Godzilla")
