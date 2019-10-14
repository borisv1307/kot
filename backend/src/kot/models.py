from django.db import models

# Create your models here.

# Monsters tend to change so they will be lookup 
class Monster(models.Model):
    monster_name = models.CharField(max_length=30)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    
# load all 66 Cards     
class Card(models.Model):
    card_details = models.CharField(max_length=30)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

class User(models.Model):
    #ids are better for realtionship and reference, they are auto created in all classes
    #user_id = models.AutoField(primary_key=True)
    user_monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    #the user can be an email or guest thus username 
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    
class Game(models.Model):
    GAME_RESULT = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('I', 'In-Progress'),
    )
    MONSTER_POSITION = (
        ('T', 'In-Tokyo'),
        ('O', 'Outside-Tokyo'),
    )
    #game_id = models.IntegerField(primary_key=True)
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=1, choices=MONSTER_POSITION)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    is_winner = models.CharField(max_length=1, choices=GAME_RESULT)
    #class Meta:
    #    unique_together = (('game_id', 'user'),)

class Dice(models.Model):
    DICE_VALUE = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Two'),
        ('4', 'Energy'),
        ('5', 'Attack'),
        ('6', 'Heal'),
    )
    DICE_SELECT = (
        ('Y', 'Selected'),
        ('N', 'Not-Selected'),
    )
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dice1 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice1_selected = models.CharField(max_length=1, choices=DICE_SELECT)
    Dice2 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice2_selected = models.CharField(max_length=1, choices=DICE_SELECT)
    Dice3 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice3_selected = models.CharField(max_length=1, choices=DICE_SELECT)
    Dice4 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice4_selected = models.CharField(max_length=1, choices=DICE_SELECT)
    Dice5 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice5_selected = models.CharField(max_length=1, choices=DICE_SELECT)
    Dice6 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice6_selected = models.CharField(max_length=1, choices=DICE_SELECT)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    
    
class Play(models.Model):
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # should cascade be applied below.
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    victory_points = models.IntegerField()
    energy_cube = models.IntegerField()
    life_points = models.IntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField() 
 
