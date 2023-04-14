# tweet/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('detailpost/<int:id>', views.detail_post, name='detail_post'),
    path('detailpost/delete/<int:id>', views.delete_post, name='delete_post'),
    path('detailpost/update/<int:id>', views.update_post, name='update_post')
]