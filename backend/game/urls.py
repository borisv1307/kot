from django.conf.urls import url
from django.urls import path

from . import views, game_views

urlpatterns = [
    path('game/view/', game_views.GameView.as_view()),
    path('game/list/', game_views.GameList.as_view()),
    path('game/detail/<str:pk>/', game_views.GameDetail.as_view()),
    path('dice/', views.views_rest.roll_dice),
    url(r'^', views.FrontendAppView.as_view()),
]
