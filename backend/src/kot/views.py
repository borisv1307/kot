from rest_framework import generics

from .models import Dice
from .models import Game
from .models import Play
from .models import Player
from .serializers import DiceSerializer
from .serializers import GameSerializer
from .serializers import PlaySerializer
from .serializers import PlayerSerializer


class ListPlayer(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class DetailPlayer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ListDice(generics.ListCreateAPIView):
    queryset = Dice.objects.all()
    serializer_class = DiceSerializer


class DetailDice(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dice.objects.all()
    serializer_class = DiceSerializer


class ListGame(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class DetailGame(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ListPlay(generics.ListCreateAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class DetailPlay(generics.RetrieveUpdateDestroyAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
