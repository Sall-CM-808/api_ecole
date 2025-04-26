from rest_framework import serializers

from .models import NoteCours, NoteCompos


class NoteCoursSerializers(serializers.ModelSerializer):
    class Meta:
        model = NoteCours
        fields = "__all__"

    #note doit etre supperieur a 0
    def validate_value_note_cours(self, value1, value2):
        if value1 or value2 < 0 :
            raise serializers.ValidationError("La note doit être suppérieur à 0")


class NoteComposSerializers(serializers.ModelSerializer):
    class Meta:
        model = NoteCompos
        fields = "__all__"

    def validate_note_compos(self, value):
        raise serializers.ValidationError("La note doit être suppérieur à 0")
