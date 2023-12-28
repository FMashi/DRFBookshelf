from django.shortcuts import render
from rest_framework import mixins, viewsets
from .serializers import *
from .models import *


# Create your views here.
class NewsViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
