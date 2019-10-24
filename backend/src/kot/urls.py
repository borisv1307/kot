from django.urls import path

from . import views

# from .views import ListPlayer, DetailPlayer, ListDice, DetailDice, ListGame, DetailGame, ListPlay, DetailPlay

urlpatterns = [
    path('player', views.ListPlayer.as_view()),
    path('<int:pk>/', views.DetailPlayer.as_view()),
    path('dice', views.ListDice.as_view()),
    path('<int:pk>/', views.DetailDice.as_view()),
    path('game', views.ListGame.as_view()),
    path('<int:pk>/', views.DetailGame.as_view()),
    path('play', views.ListPlay.as_view()),
    path('<int:pk>/', views.DetailPlay.as_view()),

]
