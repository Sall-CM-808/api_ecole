from django.db import models

from matiere.models import Matiere

from classe.models import Classe


# Create your models here.


class Examen(models.Model):
    #libelle, ex: Evaluation 1er trimestre...
    libelle = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
