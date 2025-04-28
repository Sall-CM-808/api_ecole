from django.db import models

from  matiere.models import Matiere

from evaluation.models import Evaluation


# Create your models here.

#les notes de cours
class NoteCours(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    valeur_note_cours_orale = models.DecimalField(default=0,decimal_places=2, max_digits=5)
    valeur_note_cours_ecrite = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    date_enreg = models.DateTimeField(auto_now_add=True)


#les notes de la composition
class NoteCompos(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    valeur_note_compos = models.DecimalField(max_digits=5, decimal_places=2)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    date_enreg = models.DateTimeField(auto_now_add=True)
