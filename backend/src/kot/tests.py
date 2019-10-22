# import pytest
from django.test import TestCase

from .models import User


class UserModelTest(TestCase):

    # @pytest.fixture()
    # @pytest.mark.django_db
    @classmethod
    def setUpUser(cls):
        # super(UserModelTest, cls).setUpClass()
        User.objects.create(monster_name='Godzilla')
        User.objects.create(username='User1')
        User.objects.create(password='Password1')
        # User.objects.create(date_created=datetime.datetime.now())
        # User.save()

    def test_user_content(self):
        user = User.objects.filter(monster_name='Godzilla')
        expected_object_name = f'{user.monster_name}'
        self.assertEquals(expected_object_name, "Godzilla")
