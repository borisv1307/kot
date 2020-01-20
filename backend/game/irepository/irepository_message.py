class IRepositoryMessage:
    def __init__(self):
        self.message = None
        self.message_id = None

    """
    CRUD function for Message below
    """

    def save_message_db(self, message):
        pass

    def get_message_db(self, message_id):
        pass

    def update_message_db(self, message, message_id):
        pass

    def delete_message_db(self, message_id):
        pass
