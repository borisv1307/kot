from rest_framework import serializers

from . import models


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'room_name',
            'game_status',
            'first_winner',
            'second_winner',
            'third_winner',
            'fourth_winner',
            'fifth_winner',
            'sixth_winner',
            'date_created',
        )
        model = models.Game


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'game',
            'monster_name',
            'username',
            'online',
            'date_created',
        )
        model = models.User


class DiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'user',
            'roll_number',
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
            'dice7',
            'dice7_selected',
            'dice8',
            'dice8_selected',
            'date_created',
        )
        model = models.Dice


class PlaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'user',
            'card1_swept',
            'card1_swept_type',
            'card2_swept',
            'card2_swept_type',
            'card3_swept',
            'card3_swept_type',
            'card_purchased',
            'card_purchased_type',
            'card_used',
            'card_used_type',
            'location',
            'victory_points',
            'energy_cube',
            'life_points',
            'date_created',
        )
        model = models.Play


class RollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'user',
            'roll_number',
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
            'dice7',
            'dice7_selected',
            'dice8',
            'dice8_selected',
            'date_created',
        )
        model = models.Dice
