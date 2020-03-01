import datetime

from game.models import Game
from game.models import User
from game.player.player import Player


class IRepositoryPlayer:
    def __init__(self):
        self.user = None

    def save_player(self, player: Player, room):
        self.user = User(game=Game.objects.get(room_name=room),
                         monster_name=player.monster_name,
                         username=player.username,
                         date_created=datetime.datetime.now())
        self.user.save()
        return self.user

    def get_player_by_id(self, user_id):
        self.user = User.objects.get(id=user_id)
        return self.user

    def get_players_by_player_and_room(self, player: Player, room):
        self.user = User.objects.get(monster_name=player.monster_name, game=Game.objects.get(room_name=room).id)
        return self.user

    def update_player_username(self, name, user_id):
        self.user = User.objects.get(id=user_id)
        self.user.username = name
        self.user.save()
        return self.user

    def update_player_monster_name(self, monster, user_id):
        self.user = User.objects.get(id=user_id)
        self.user.monster_name = monster
        self.user.save()
        return self.user

    def delete_player_by_id(self, user_id):
        self.user = User.objects.get(id=user_id)
        self.user.delete()
        return None
