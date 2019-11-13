from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat$', consumers.ChatConsumer),
    re_path(r'ws/lobby/(?P<room_name>\w+)/$', consumers.GameConsumer),
]
