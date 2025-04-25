from django.db import models

from  matiere.models import Matiere

# Create your models here.


class Note(models.Model):
    #type de note
    class Note(models.Model):
        # la matiere
        matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
        valeur = models.DecimalField(max_digits=5, decimal_places=2)
        #libelle --> exemple: note cours , note compos, devoirs
        libelle = models.CharField(max_length=100)
        creat_at = models.DateTimeField(auto_now_add=True)
        type_note = models.CharField(max_length=10, choices=[
                ('cours', 'Note de cours'),
                ('compo', 'Note de composition'),
            ])
        update_at = models.DateTimeField(auto_now_add=True)
