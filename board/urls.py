from  django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create_feed_view, name='create-feed'),
]