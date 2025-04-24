from django.db import models
from user.models import User
from matiere.models import Subjects
from classe.models import Classes

# Create your models here.

class Professors(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    level = models.ForeignKey(Classes,on_delete=models.CASCADE)
