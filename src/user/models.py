from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(null=True,blank=True)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="profile_pictures",null=True,blank=True)
    role = models.CharField(max_length=100,choices=[('professor','Professeur'),('student','Eleve'),('manager',"Gestionnaire de l''Etablissement")])
