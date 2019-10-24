from django.contrib import admin

from .models import Player, Dice, Game, Play

admin.site.register(Player)
admin.site.register(Dice)
admin.site.register(Game)
admin.site.register(Play)
# Register your models here.
