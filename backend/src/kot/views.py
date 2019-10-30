from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers

# from ..kot import roll

# from backend.src.kot.game.dice.dice import roll

# Create your views here.


@api_view(['GET'])
def roll_dice(request):
    if request.method == 'GET':

        # dto = models.Todo()
        # dto.description = 'asdfsaasdfsfsadfasd'
        # serializer = serializers.MessageSerializer(dto)
        # return Response(serializer.data)

        dto = models.Dice()
        dto.dice1 = '1'  # roll()
        dto.dice1_selected = True
        dto.dice2 = '2'  # roll()
        dto.dice2_selected = False
        dto.dice3 = '3'  # roll()
        dto.dice3_selected = True
        dto.dice4 = 'c'  # roll()
        dto.dice4_selected = False
        dto.dice5 = 'h'  # roll()
        dto.dice5_selected = True
        dto.dice6 = 'e'  # roll()
        dto.dice6_selected = False
        serializer = serializers.RollSerializer(dto)
        return Response(serializer.data)

        # user='dice.roll()', dice1='dice.roll()', dice2=dice.roll(        ), dice3='dice.roll()', dice4='dice.roll()', dice5='dice.roll()', dice6='dice.roll()'
        # roll = models.Dice()
        # roll.save()
        # serializer = serializers.DiceSerializer(roll)
        # return Response('{asdf}')
