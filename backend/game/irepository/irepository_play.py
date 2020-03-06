import datetime

from game.models import Game
from game.models import Play
from game.models import User
from game.player.player import Player


class IRepositoryPlay:

    def __init__(self):
        self.play = None
        self.location = None

    def save_play_card_swept(self, username, room, card1, card1_type, card2, card2_type, card3, card3_type, location,
                             victory_points, energy, health):
        self.play = Play(user=User.objects.get(username=username, game=Game.objects.get(room_name=room)),
                         card1_swept=card1,
                         card1_swept_type=card1_type,
                         card2_swept=card2,
                         card2_swept_type=card2_type,
                         card3_swept=card3,
                         card3_swept_type=card3_type,
                         location=location,
                         victory_points=victory_points,
                         energy_cube=energy,
                         health_points=health,
                         date_created=datetime.datetime.now())
        self.play.save()
        return self.play

    def save_play_card_purchased(self, username, room, card, card_type, location, victory_points, energy, health):
        self.play = Play(user=User.objects.get(username=username, game=Game.objects.get(room_name=room)),
                         card_purchased=card,
                         card_purchased_type=card_type,
                         location=location,
                         victory_points=victory_points,
                         energy_cube=energy,
                         health_points=health,
                         date_created=datetime.datetime.now())
        self.play.save()
        return self.play

    def save_play_card_used(self, username, room, card, card_type, location, victory_points, energy, health):
        self.play = Play(user=User.objects.get(username=username, game=Game.objects.get(room_name=room)),
                         card_used=card,
                         card_used_type=card_type,
                         location=location,
                         victory_points=victory_points,
                         energy_cube=energy,
                         health_points=health,
                         date_created=datetime.datetime.now())
        self.play.save()
        return self.play

    def get_play_by_id(self, play_id):
        self.play = Play.objects.get(id=play_id)
        return self.play

    def get_plays_by_player_and_room(self, username, room):
        self.play = Play.objects.get(user=User.objects.get(username=username,
                                                           game=Game.objects.get(room_name=room)).id)
        return self.play

    def update_play_card_swept_by_id(self, play_id, card1, card1_type, card2, card2_type, card3, card3_type):
        self.play = Play.objects.get(id=play_id)
        self.play.card1_swept = card1
        self.play.card1_swept_type = card1_type
        self.play.card2_swept = card2
        self.play.card2_swept_type = card2_type
        self.play.card3_swept = card3
        self.play.card3_swept_type = card3_type
        self.play.save()
        return self.play

    def update_play_card_purchased_by_id(self, play_id, card, card_type):
        self.play = Play.objects.get(id=play_id)
        self.play.card_purchased = card
        self.play.card_purchased_type = card_type
        self.play.save()
        return self.play

    def update_play_card_used_by_id(self, play_id, card, card_type):
        self.play = Play.objects.get(id=play_id)
        self.play.card_used = card
        self.play.card_used_type = card_type
        self.play.save()
        return self.play

    def update_play_location_by_id(self, play_id, location_value):
        self.play = Play.objects.get(id=play_id)
        self.play.location = location_value
        self.play.save()
        return self.play

    def update_play_victory_points_by_id(self, play_id, victory_value):
        self.play = Play.objects.get(id=play_id)
        self.play.victory_points = victory_value
        self.play.save()
        return self.play

    def update_play_energy_by_id(self, play_id, energy_value):
        self.play = Play.objects.get(id=play_id)
        self.play.energy_cube = energy_value
        self.play.save()
        return self.play

    def update_play_health_by_id(self, play_id, health_value):
        self.play = Play.objects.get(id=play_id)
        self.play.health_points = health_value
        self.play.save()
        return self.play

    def delete_play_by_id(self, play_id):
        self.play = Play.objects.get(id=play_id)
        self.play.delete()
        return None
