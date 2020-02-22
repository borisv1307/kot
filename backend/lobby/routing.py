from django.urls import re_path

from . import consumers
from . import consumers_lobby

websocket_urlpatterns = [
    re_path(r'ws/lobby/(?P<room_name>\w+)/$', consumers_lobby.LobbyConsumer),
    re_path(r'ws/game/(?P<room_name>\w+)/$', consumers.GameConsumer),
]
