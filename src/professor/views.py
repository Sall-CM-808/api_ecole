from django.shortcuts import render
from rest_framework import generics,mixins
from professor.models import Professors
from professor.serializer import ProfessorCreationSerializer

# Create your views here.

#La vue qui permet de creer de voir un et tous les professeurs de la table professeur
class ProfessorMixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
):
    queryset = Professors.objects.all()
    serializer_class = ProfessorCreationSerializer
    
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