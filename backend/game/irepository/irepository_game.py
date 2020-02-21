import datetime

from game.models import Game


class IRepositoryGame:
    def __init__(self):
        self.game = None

    def save_game(self, room):
        self.game = Game(room_name=room,
                         game_status='2',
                         first_winner=0,
                         second_winner=0,
                         third_winner=0,
                         fourth_winner=0,
                         fifth_winner=0,
                         sixth_winner=0,
                         date_created=datetime.datetime.now())
        self.game.save()
        return self.game.id

    def get_game_by_id(self, game_id):
        self.game = Game.objects.get(id=game_id)
        return self.game

    def get_game_by_status(self, status_type):
        self.game = Game.objects.filter(game_status=status_type)
        return self.game

    def get_game_by_room(self, room):
        self.game = Game.objects.filter(room_name=room)
        return self.game

    def get_all_games(self):
        self.game = Game.objects.get()
        return self.game

    def update_game_status_by_id(self, game_id, status):
        self.game = Game.objects.get(id=game_id)
        self.game.game_status = status
        self.game.save()
        return self.game

    def update_game_winners_by_id(self, game_id, first, second, third, fourth, fifth, sixth):
        self.game = Game.objects.get(id=game_id)
        self.game.first_winner = first
        self.game.second_winner = second
        self.game.third_winner = third
        self.game.fourth_winner = fourth
        self.game.fifth_winner = fifth
        self.game.sixth_winner = sixth
        self.game.save()
        return self.game

    def delete_game_by_id(self, game_id):
        self.game = Game.objects.get(id=game_id)
        self.game.delete()
        return None
