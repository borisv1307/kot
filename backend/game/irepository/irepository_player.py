import datetime

from game.models import User
from game.player.player import Player


class IRepositoryPlayer:
    def __init__(self):
        self.player = Player()

    """
    CRUD function for Player below
    """

    def save_player_db(self, player: Player):
        self.player = player
        user = User(monster_name=player.monster_name,
                    username=player.username,
                    password=player.password,
                    date_created=datetime.datetime.now())
        user.save()
        return user

    def get_player_db(self, player: Player):
        self.player = player
        user = User.objects.get(monster_name=player.monster_name)
        return user

    def update_player_db(self, player: Player):
        self.player = player
        user = User.objects.get(monster_name=player.monster_name)
        user.username = player.username
        user.password = player.password
        user.save()
        return user

    def delete_player_db(self, player: Player):
        self.player = player
        user = User.objects.get(monster_name=player.monster_name)
        user.delete()
        return None
