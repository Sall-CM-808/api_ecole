from django.shortcuts import render
from rest_framework import viewsets

from .models import Matiere
from .serializers import MatiereSerializers


# Create your views here.


class MatiereViewsSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializers
