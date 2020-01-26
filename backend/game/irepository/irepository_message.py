import datetime

from game.models import Message


class IRepositoryMessage:
    def __init__(self):
        ##self.message = None
        self.type = None

    """
    CRUD function for Player below
    """

    def save_message_db(self, message_string, message_type):
        self.type = message_type
        message = Message(message_string=message_string,
                          message_type=message_type,
                          date_created=datetime.datetime.now())
        message.save()
        return message

    def get_message_db(self, message_string, message_type):
        self.type = message_type
        message = Message.objects.get(message_string=message_string,
                                      message_type=message_type)
        return message

    def update_message_db(self, message_string, message_type):
        self.type = message_type
        message = Message.objects.get(message_string=message_string,
                                      message_type=message_type)
        message.message_string = message_string
        message.message_type = message_type
        message.save()
        return message

    def delete_message_db(self, message_string, message_type):
        self.type = message_type
        message = Message.objects.get(message_string=message_string,
                                      message_type=message_type)
        message.delete()
        return None
