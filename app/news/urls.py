from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
    path('news/', include('news.urls')),
    path('news/<int:pk>/', include('news.urls')),
]