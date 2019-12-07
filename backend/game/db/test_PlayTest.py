import datetime

import pytest
from django.test import TestCase
from django.utils import timezone

from game.models import Dice
from game.models import Game
from game.models import Play
from game.models import User

@pytest.mark.django_db
class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        player = User.objects.create(monster_name='Godzilla',
                                       username='User1',
                                       password='Password1',
                                       date_created=timezone.now())

        game = Game.objects.create(user=player,
                                   is_winner='Y',
                                   num_players='10',
                                   player_position='1',
                                   date_created=timezone.now(),
                                   date_modified=timezone.now())

        dice = Dice.objects.create(user=player,
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

        Play.objects.create(user=player,
                            game=game,
                            dice=dice,
                            card_purchased='Card1',
                            card_used='Card2',
                            location='T',
                            victory_points='20',
                            energy_cubes='30',
                            life_points='40',
                            date_created=timezone.now())

    def test_user_content(self):
        play = Play.objects.get(user=1)
        expected_object_name = f'{play.location}'
        self.assertEqual(expected_object_name, 'T')
