from django.db import models
from user.models import User
# Create your models here.

class Students(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    classe = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.username)