from django.shortcuts import render
from student.serializer import StudentCreationSerializer
from student.models import Students
from rest_framework import mixins, generics

# Create your views here.

class StudentMixin(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Students.objects.all()
    serializer_class = StudentCreationSerializer
    
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