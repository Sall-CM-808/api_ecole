from rest_framework import serializers

from .models import Note


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

    #note doit etre supperieur a 0
    def validate_value_note(self, value):
        if value < 0 :
            raise serializers.ValidationError("La note doit être suppérieur à 0")
