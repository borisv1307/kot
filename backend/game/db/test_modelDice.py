import pytest
from django.test import TestCase
from django.utils import timezone

from game.db.db_action import dice_roll_to_db
from game.dice_handler import DiceHandler
from game.models import Dice
from game.models import User


@pytest.mark.django_db
class PlayerModelTest(TestCase):

    @classmethod
    def setUp(cls):
        user = User.objects.create(monster_name='Godzilla',
                                   username='User1',
                                   password='Password1',
                                   date_created=timezone.now())

        # Dice.objects.create(user=user,
        #                     dice1='1',
        #                     dice1_selected='Y',
        #                     dice2='1',
        #                     dice2_selected='Y',
        #                     dice3='1',
        #                     dice3_selected='Y',
        #                     dice4='1',
        #                     dice4_selected='Y',
        #                     dice5='1',
        #                     dice5_selected='Y',
        #                     dice6='1',
        #                     dice6_selected='Y',
        #                     date_created=timezone.now())

    def test_user_content(self):
        dice = Dice.objects.get(user=1)
        expected_object_name = f'{dice.dice1}'
        self.assertEqual(expected_object_name, '1')

    def test_three_dice_rolls_to_db(self):
        test_dice_handler = DiceHandler()
        test_dice_handler.roll_initial(6, 3)
        initial_dice_values = test_dice_handler.dice_values
        dice_roll_to_db(initial_dice_values, [])

        dice_to_re_roll_indexes = [0, 1, 2]

        test_dice_handler.re_roll_dice(dice_to_re_roll_indexes)
        second_dice_values = test_dice_handler.dice_values
        dice_roll_to_db(second_dice_values, dice_to_re_roll_indexes)

        test_dice_handler.re_roll_dice(dice_to_re_roll_indexes)
        third_dice_values = test_dice_handler.dice_values
        dice_roll_to_db(third_dice_values, dice_to_re_roll_indexes)

        results = Dice.objects.all()
        self.assertTrue(len(results) == 3)
        self.assertEqual(results[0].dice1, str(initial_dice_values[0]))
