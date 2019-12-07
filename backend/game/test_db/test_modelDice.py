import datetime

import pytest
from django.test import TestCase
from django.utils import timezone

from game.models import Dice
from game.models import User


@pytest.mark.django_db
class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        player = User.objects.create(monster_name='Godzilla',
                                       username='User1',
                                       password='Password1',
                                       date_created=timezone.now())

        Dice.objects.create(user=player,
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
                            date_created=timezone.now())

    def test_user_content(self):
        dice = Dice.objects.get(user=1)
        expected_object_name = f'{dice.dice1}'
        self.assertEquals(expected_object_name, '1')
