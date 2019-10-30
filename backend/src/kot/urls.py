from django.urls import path

from . import views

urlpatterns = [
    path('dice/', views.roll_dice),
]
