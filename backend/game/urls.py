from django.urls import path

from . import views

urlpatterns = [
    path('dice/', views.views_rest.roll_dice),
]
