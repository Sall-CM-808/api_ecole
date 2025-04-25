from django.db import models

# le model "classe" qui represente une sallle de classe


class Classe(models.Model):
    # nom de la salle
    nom = models.CharField(max_length=100)
    annee_scolaire = models.CharField(max_length=9)
    niveau = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"nom: {self.nom} \nannee_scolaire: {self.annee_scolaire}"