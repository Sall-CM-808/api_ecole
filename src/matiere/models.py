from django.db import models

# Create your models here.


class Matiere(models.Model):

    nom = models.CharField(max_length=100)
    poid_note_cours = models.IntegerField(default=1)
    poid_note_compos = models.IntegerField(default=1)

    def __str__(self):
        return self.nom
