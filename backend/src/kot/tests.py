from django.test import TestCase
from datetime import date
from .models import User


# Create your tests here.
class UserModelTest(TestCase):

    def setUp(self):
        self.username = "testuser"
        self.password = "testPassword"
        self.date_created = date.today()
        self.date_modified = date.today()

        self.test_user = User.objects.create(
            username=self.username,
            password=self.password,
            date_created=self.date_created,
            date_modified=self.date_modified
        )

    def test_user_model(self):
        user = self.test_user
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.date_modified, self.date_modified)
        self.assertEqual(user.date_created, self.date_created)
        self.assertEqual(user.password, self.password)