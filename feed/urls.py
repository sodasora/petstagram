from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage_feed, name='mainpage_feed'),
]
