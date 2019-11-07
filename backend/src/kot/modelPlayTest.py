import datetime

from django.test import TestCase

from .models import Dice
from .models import Game
from .models import Play
from .models import Player


class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        player = Player.objects.create(monster_name='Godzilla',
                                       username='User1',
                                       password='Password1',
                                       date_created=datetime.datetime.now())

        game = Game.objects.create(player=player,
                                   is_winner='Y',
                                   num_players='10',
                                   player_position='1',
                                   date_created=datetime.datetime.now(),
                                   date_modified=datetime.datetime.now())

        dice = Dice.objects.create(player=player,
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
                                   date_created=datetime.datetime.now())

        Play.objects.create(player=player,
                            game=game,
                            dice=dice,
                            card_purchased='Card1',
                            card_used='Card2',
                            location='T',
                            victory_points='20',
                            energy_cubes='30',
                            life_points='40',
                            date_created=datetime.datetime.now())

    def test_user_content(self):
        play = Play.objects.get(player=1)
        expected_object_name = f'{play.location}'
        self.assertEquals(expected_object_name, 'T')
