from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import register_user, user_login, user_logout

router = DefaultRouter()
router.register('author', AuthorViewSet)
router.register('publish', PublisherViewSet)
router.register('faculty', FacultyViewSet)
router.register('language', LanguageViewSet)
router.register('category', CategoryViewSet)
router.register('section', SectionViewSet)
router.register('book', BookViewSet)
router.register('ebook', EBookViewSet)
router.register('copy', CopyViewSet)

urlpatterns = [
    path('book/', include(router.urls)),
    path('book/<int:pk>/', include(router.urls))

]