from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage_view, name='mypage'),
    path('mypage_update/', views.mypage_update_view, name='mypage_update'),
]