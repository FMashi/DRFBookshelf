from django.urls import path
from .views import (
    user_list, 
    user_details,
    register_user,
    user_login,
    user_logout,
    change_password,
    )




urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_details, name='user_details'),
    path('register/', register_user, name='register_user'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
]