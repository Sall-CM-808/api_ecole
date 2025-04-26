from django.db import models

# Create your models here.


class Evaluation(models.Model):
    #ex: Evaluation du 1er semestre
    nom = models.CharField(max_length=100)
    #poid du cours
    poid_note_cours = models.IntegerField(default=1)
    #poid du compos
    poid_note_compos = models.IntegerField(default=1)
    #notation ex: /20
    notation = models.IntegerField(default=20)
    date_enreg = models.DateTimeField(auto_now_add=True, null=True)

