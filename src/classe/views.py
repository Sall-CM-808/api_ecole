from django.shortcuts import render
from rest_framework import viewsets

from .models import Classe
from .serializers import ClasseSerializers


# Create your views here.

class ClasseViewsSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializers

