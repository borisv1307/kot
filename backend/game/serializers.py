from rest_framework import serializers
from django.core.serializers.json import Serializer
from . import models


class DiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'delimitedRoll',
        )
        model = models.Dice


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            # 'id',
            'message_type',
            'message_string',
            'date_created',
        )
        model = models.Message


class RollSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'user',
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
            'date_created',
            'allowReroll',
        )
        model = models.Dice
