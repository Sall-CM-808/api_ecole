from django.db import models
from user.models import User

# Create your models here.

class SchoolManager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    poste = models.CharField(max_length=255)