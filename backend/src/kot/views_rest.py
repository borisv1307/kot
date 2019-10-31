from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers

import random

# No UI views, see frontend for React UI.

# REST Endpoint Views...


@api_view(['GET'])
def roll_dice(request):
    if request.method == 'GET':
        # temp intend to utilize game.dice.dice.roll()
        options = ['1', '2', '3', 'e', 'a', 'h']

        dto = models.Dice()
        dto.dice1 = random.choice(list(options))  # roll()
        dto.dice1_selected = True
        dto.dice2 = random.choice(list(options))  # roll()
        dto.dice2_selected = False
        dto.dice3 = random.choice(list(options))  # roll()
        dto.dice3_selected = True
        dto.dice4 = random.choice(list(options))  # roll()
        dto.dice4_selected = False
        dto.dice5 = random.choice(list(options))  # roll()
        dto.dice5_selected = True
        dto.dice6 = random.choice(list(options))  # roll()
        dto.dice6_selected = False
        serializer = serializers.RollSerializer(dto)
        return Response(serializer.data)
