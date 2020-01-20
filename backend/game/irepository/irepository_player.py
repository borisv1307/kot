import datetime

from game.models import User
from game.player.player import Player


class IRepositoryPlayer:
    def __init__(self):
        self.player = None
        self.player_id = None

    """
    CRUD function for Player below
    """

    def save_player_db(self, player: Player):
        self.player = player
        User.monster_name = 'Test'
        User.username = 'Test'
        User.password = 'Test'
        User.date_created = datetime.datetime.now()
        User.save()
        pass

    def get_player_db(self, player_id):
        pass

    def update_player_db(self, player, player_id):
        pass

    def delete_player_db(self, player_id):
        pass
