import datetime

from game.models import Game
from game.models import User
from game.player.player import Player


class IRepositoryPlayer:
    def __init__(self):
        self.user = None

    def save_player(self, username, room):
        self.user = User(game=Game.objects.get(room_name=room),
                         ##monster_name=Null,
                         username=username,
                         date_created=datetime.datetime.now())
        self.user.save()
        return self.user

    def get_player_by_id(self, user_id):
        self.user = User.objects.get(id=user_id)
        return self.user

    def get_players_by_username_and_room(self, username, room):
        self.user = User.objects.get(username=username, game=Game.objects.get(room_name=room).id)
        return self.user

    def update_player_username_by_id(self, user_id, name):
        self.user = User.objects.get(id=user_id)
        self.user.username = name
        self.user.save()
        return self.user

    def update_player_username_by_username(self, username, name):
        self.user = User.objects.get(username=username)
        self.user.username = name
        self.user.save()
        return self.user

    def update_player_monster_name_by_id(self, user_id, monster):
        self.user = User.objects.get(id=user_id)
        self.user.monster_name = monster
        self.user.save()
        return self.user

    def update_player_monster_name_by_username(self, username, monster):
        self.user = User.objects.get(username=username)
        self.user.monster_name = monster
        self.user.save()
        return self.user

    def delete_player_by_id(self, user_id):
        self.user = User.objects.get(id=user_id)
        self.user.delete()
        return None

    def delete_player_by_username(self, username):
        self.user = User.objects.get(username=username)
        self.user.delete()
        return None
