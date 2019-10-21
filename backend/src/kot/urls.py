from django.urls import path

from . import views

# from .views import ListUser, DetailUser, ListDice, DetailDice, ListGame, DetailGame, ListPlay, DetailPlay

urlpatterns = [
    path('', views.ListUser.as_view()),
    path('<int:pk>/', views.DetailUser.as_view()),
    path('', views.ListDice.as_view()),
    path('<int:pk>/', views.DetailDice.as_view()),
    path('', views.ListGame.as_view()),
    path('<int:pk>/', views.DetailGame.as_view()),
    path('', views.ListPlay.as_view()),
    path('<int:pk>/', views.DetailPlay.as_view()),

]
