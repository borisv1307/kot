from rest_framework import serializers

from .models import Dice
from .models import Game
from .models import Play
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'monster_name',
            'username',
            'password',
            'date_created'
        )
        model = Player


class DiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'player',
            'dice1',
            'dice1_selected',
            'dice2',
            'dice2_selected',
            'dice3',
            'dice3_selected',
            'dice4',
            'dice4_selected',
            'dice5',
            'dice5_selected',
            'dice6',
            'dice6_selected',
            'date_created'
        )
        model = Dice


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'player',
            'is_winner',
            'num_players',
            'player_position',
            'date_created',
            'date_modified'
        )
        model = Game


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'player',
            'game',
            'dice',
            'card_purchased',
            'card_used',
            'location',
            'victory_points',
            'energy_cubes',
            'life_points',
            'date_created'
        )
        model = Play
