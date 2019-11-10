from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    path('dice/', views.views_rest.roll_dice),
    url(r'^',views.FrontendAppView.as_view()),
]