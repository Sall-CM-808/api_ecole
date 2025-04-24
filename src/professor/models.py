from django.db import models
from user.models import User
from matiere.models import Subjects
from classe.models import Classes
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Professors(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    level = models.ForeignKey(Classes,on_delete=models.CASCADE)
    phone_nuber = PhoneNumberField(unique=True,default='+224')