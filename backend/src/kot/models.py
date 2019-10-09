from django.core.validators import EmailValidator, validate_email, MinLengthValidator
from django.db import models


# Create your models here.

class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50, default="sample@drexel.edu",
                             validators=[validate_email])
    password = models.CharField(max_length=30, validators=[MinLengthValidator(8)])
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()


class Game(models.Model):
    GAME_RESULT = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('I', 'In-Progress'),
    )
    game_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    is_winner = models.CharField(max_length=1, choices=GAME_RESULT)

    class Meta:
        unique_together = (('game_id', 'user'),)
