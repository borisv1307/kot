import datetime

from game.models import User
from game.models import Play
from game.player.player import Player


class IRepositoryPlay:

    def __init__(self):
        self.play = None
        self.location = None

    def save_play_db(self, player: Player):
        self.play = Play(user=User.objects.get(monster_name=player.monster_name),
                         cards=player.cards,
                         location=player.location,
                         victory_points=player.victory_points,
                         energy_cube=player.energy,
                         life_points=player.current_health,
                         date_created=datetime.datetime.now())
        self.play.save()
        return self.play

    def get_play_db(self, player: Player):
        self.play = Play.objects.get(user=User.objects.get(monster_name=player.monster_name).id)
        return self.play

    def update_play_db(self, player: Player):
        self.play = Play.objects.get(user=User.objects.get(monster_name=player.monster_name).id)
        self.play.cards = player.cards
        self.play.location = player.location
        self.play.victory_points = player.victory_points
        self.play.energy_cube = player.energy
        self.play.life_points = player.current_health
        self.play.save()
        return self.play

    def delete_play_db(self, player: Player):
        self.play = Play.objects.get(user=User.objects.get(monster_name=player.monster_name).id)
        self.play.delete()
        return None
