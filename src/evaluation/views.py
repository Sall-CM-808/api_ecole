from django.shortcuts import render
from rest_framework import viewsets

from .models import Evaluation
from .serializers import EvaluationSerializers


# Create your views here.

class EvaluationViewsSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializers

