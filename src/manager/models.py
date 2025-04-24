from django.db import models
from user.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class SchoolManagers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    poste = models.CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True,default='+224')