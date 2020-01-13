from django.contrib import admin

from .models import User, Game, Dice, Play

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Dice)
admin.site.register(Play)
# Register your models here.
