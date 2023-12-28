from django.shortcuts import render
from .models import Libraries
from .serializers import LibrariesSerializer
from rest_framework import viewsets

class LibrariesViewSet(viewsets.ModelViewSet):
    queryset = Libraries.objects.all()
    serializer_class = LibrariesSerializer