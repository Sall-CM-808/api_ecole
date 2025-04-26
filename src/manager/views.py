from django.shortcuts import render
from manager.models import SchoolManagers
from manager.serializer import SchoolManagerCreationSerializer

from rest_framework import generics,mixins
# Create your views here.

class SchoolManagerMixin(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = SchoolManagerCreationSerializer
    queryset = SchoolManagers.objects.all()
    
    def get(self,request,*args,**kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)