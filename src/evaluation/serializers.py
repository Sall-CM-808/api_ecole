from rest_framework import serializers

from .models import Evaluation


class EvaluationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


