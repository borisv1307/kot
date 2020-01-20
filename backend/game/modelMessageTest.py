import datetime

from django.test import TestCase

from game.models import Message


class PlayModelTest(TestCase):

    @classmethod
    def setUp(cls):
        Message.objects.create(message_type='game',
                                         message_string='Game Over',
                                         date_created=datetime.datetime.now())

    def test_message_content(self):
        message = Message.objects.get(message_type='game')
        expected_object_name = f'{message.message_string}'
        self.assertEquals(expected_object_name, 'Game Over')
