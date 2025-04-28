from django.shortcuts import render
from rest_framework import viewsets

from .models import NoteCours, NoteCompos
from .serializers import NoteCoursSerializers, NoteComposSerializers


# Create your views here.


class NoteCoursViewsSet(viewsets.ModelViewSet):
    queryset = NoteCours.objects.all()
    serializer_class = NoteCoursSerializers



class NoteComposViewsSet(viewsets.ModelViewSet):
    queryset = NoteCompos.objects.all()
    serializer_class = NoteComposSerializers

