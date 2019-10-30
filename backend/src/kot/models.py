from django.db import models


# Create your models here.
class User(models.Model):
    monster_name = models.CharField(max_length=30)
    # the user can be an email or guest thus username, guest must be unique
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_created = models.DateTimeField()


class Dice(models.Model):
    DICE_VALUE = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Two'),
        ('4', 'Energy'),
        ('5', 'Attack'),
        ('6', 'Heal'),
    )
    DICE_SELECTED = (
        ('Y', 'Selected'),
        ('N', 'Not-Selected'),
    )
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dice1 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice1_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice2 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice2_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice3 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice3_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice4 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice4_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice5 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice5_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice6 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice6_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    date_created = models.DateTimeField()


class Game(models.Model):
    GAME_RESULT = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('I', 'In-Progress'),
    )
    # game_id = models.IntegerField(primary_key=True)
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    is_winner = models.CharField(max_length=1, choices=GAME_RESULT)
    num_players = models.IntegerField()
    player_position = models.IntegerField()
    date_created = models.DateTimeField()


class Play(models.Model):
    MONSTER_POSITION = (
        ('T', 'In-Tokyo'),
        ('O', 'Outside-Tokyo'),
    )
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # should cascade be applied below.
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # should cascade be applied below.
    dice = models.ForeignKey(Dice, on_delete=models.CASCADE)
    # should cascade be applied below.
    card_purchased = models.CharField(max_length=30)
    card_used = models.CharField(max_length=30)
    location = models.CharField(max_length=1, choices=MONSTER_POSITION)
    victory_points = models.IntegerField()
    energy_cube = models.IntegerField()
    life_points = models.IntegerField()
    date_created = models.DateTimeField()


class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)
