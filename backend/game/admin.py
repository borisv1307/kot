from django.contrib import admin

from .models import User, Game, Dice, Message

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Message)
# admin.site.register(Dice)
# Register your models here.
