from django.db import models


# Create your models here.


class Subjects(models.Model):
    subject_name = models.CharField(max_length=255)