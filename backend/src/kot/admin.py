from django.contrib import admin

from .models import User, Dice, Game, Play

admin.site.register(User)
admin.site.register(Dice)
admin.site.register(Game)
admin.site.register(Play)
# Register your models here.
