from django.urls import path

import detailpost.views
from . import views

urlpatterns = [
    path('post/', views.create_feed_view, name='create-feed'),
    path('', views.mainpage_feed, name='mainpage_feed'),
    path('detailpost/<int:id>/post_comment/', views.post_comment, name='post_comment'),
    path('detailpost/post_comment/delete/<int:id>', views.post_comment_delete, name='post_comment_delete'),
    path('detailpost/post_comment/update/<int:id>', views.post_comment_update, name='post_comment_delete'),
]