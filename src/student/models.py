from django.db import models
from user.models import User
from classe.models import Classes

# Create your models here.

class Students(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    classe = models.OneToOneField(Classes,on_delete=models.CASCADE)
