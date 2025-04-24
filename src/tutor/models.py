from django.db import models
from user.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Tutors(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True)
    student = models.ForeignKey()