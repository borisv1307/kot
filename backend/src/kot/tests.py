from django.test import TestCase
from datetime import datetime
from django.utils import timezone
from .models import User, Game


# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        self.email = "kot_user@drexel.edu"
        self.password = "testPassword"
        self.date_created = datetime.now(tz=timezone.utc)
        self.date_modified = datetime.now(tz=timezone.utc)

        self.test_user = User.objects.create(
            email=self.email,
            password=self.password,
            date_created=self.date_created,
            date_modified=self.date_modified
        )

        self.game_id = 1
        self.user = self.test_user
        self.isWinner = 'N'

        self.game = Game.objects.create(
            game_id=self.game_id,
            user=self.test_user,
            date_created=self.date_created,
            date_modified=self.date_modified,
            is_winner=self.isWinner
        )

    def test_user_model(self):
        user = self.test_user
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.date_modified, self.date_modified)
        self.assertEqual(user.date_created, self.date_created)
        self.assertEqual(user.password, self.password)

    def test_game_model(self):
        game = self.game
        self.assertIsInstance(game, Game)
        self.assertEqual(game.game_id, self.game_id)
        self.assertEqual(game.user, self.user)
        self.assertEqual(game.date_created, self.date_created)
        self.assertEqual(game.date_modified, self.date_modified)
