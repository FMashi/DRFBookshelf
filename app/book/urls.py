from django.urls import path, include
from django.urls import path,include
from .views import (
    LibrariesViewSet,
    )
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Libraries', LibrariesViewSet)

urlpatterns = [
    path('', include(router.urls)),

]