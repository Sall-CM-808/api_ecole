from django.shortcuts import render
from rest_framework import generics
from user.serializer import UserCreationSerializer
from user.models import User

# Create your views here.

class UserCreateAPI(generics.CreateAPIView):
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()
    
    