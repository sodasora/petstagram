from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create_feed_view, name='create-feed'),
    path('', views.mainpage_feed, name='mainpage_feed'),
]