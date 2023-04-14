from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up_view, name='signup'),
    path('login/', views.log_in_view, name='login'),
    path('logout/', views.logout, name='logout'),
]