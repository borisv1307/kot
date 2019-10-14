from django.test import TestCase
import datetime as datetime_orig
from .models import Monster
from .models import Card
from .models import User
from .models import Game
from .models import Dice
from kot.models import Play

class monster_model_test(TestCase):

    @classmethod
    def set_up_monster_test_data(cls):
        Monster.objects.create(monster_name="Godzilla")
        Monster.objects.create(date_created=datetime_orig.datetime.now())
        Monster.objects.create(date_modified=datetime_orig.datetime.now())

    def test_monster_content(self):
        monster = Monster.objects.get(id=1)
        expected_object_name = f'{monster.monster_name}'
        self.assertEquals(expected_object_name, "Godzilla")

        
    def today():
        return datetime.date.today()
