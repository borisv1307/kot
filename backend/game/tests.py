import datetime

from django.test import TestCase

from .models import Monster

# Create your tests here.

class MonsterModelTest(TestCase):

    @classmethod
    def set_up_monster_test_data(cls):
        Monster.objects.create(monster_name="Godzilla")
        Monster.objects.create(date_created=datetime.datetime.now())

    def test_monster_content(self):
        monster = Monster.objects.get(id=1)
        expected_object_name = f'{monster.monster_name}'
        self.assertEquals(expected_object_name, "Godzilla")
