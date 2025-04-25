from rest_framework import serializers

from .models import Matiere


class MatiereSerializers(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'

    #methode pour valider le coefficient de la matiere
    def validate_coefficient(self, value):
        if value < 0:
            raise serializers.ValidationError("Le coefficient doit être positif")

    #methode pour valider le nom de la matiere
    def validate_nom(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Le nom de la matère est trop court.")