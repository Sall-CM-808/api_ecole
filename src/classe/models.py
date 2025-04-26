from django.db import models

# Create your models here.

class Classes(models.Model):
    level_name = models.IntegerField()
    
    def __str__(self):
        return str(self.level_name)