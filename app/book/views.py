from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from .serializers import *
from .models import *


# Create your views here.
class AuthorViewSet(viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class PublisherViewSet(viewsets.GenericViewSet,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class FacultyViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()


class LanguageViewSet(viewsets.GenericViewSet,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SectionViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class BookViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class EBookViewSet(viewsets.GenericViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = EBookSerializer
    queryset = EBook.objects.all()


class CopyViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()
