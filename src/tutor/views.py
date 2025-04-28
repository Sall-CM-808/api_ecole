from django.shortcuts import render
from tutor.serializer import TutorCreationSerializer
from rest_framework import generics,mixins
from tutor.models import Tutors

# Create your views here.

class TutorMixin(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Tutors.objects.all()
    serializer_class = TutorCreationSerializer
    
    def get(self,request,*args,**kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)