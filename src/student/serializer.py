from rest_framework import serializers

from student.models import Students
from user.serializer import UserCreationSerializer

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

from django.db import transaction

#Serializer pour la creation , la vu et la suppression
class StudentCreationSerializer(serializers.ModelSerializer):
    user = UserCreationSerializer()
    class Meta:
        model = Students
        fields = ('user','classe')
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'student'
        user_serializer = UserCreationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        
        student = Students(user=None,**validated_data)
        try:
            student.full_clean(exclude=['user'])
        except DjangoValidationError as e:
            raise DRFValidationError(e.message_dict)
        
        with transaction.atomic():
            user = user_serializer.save()
            student.user = user
            student.save()
            
        return student
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        
        with transaction.atomic():
            # Mise à jour de l'eleve
            instance = super().update(instance, validated_data)
            
            # Mise à jour du User
            if user_data and getattr(instance, 'user', None):
                user_serializer = UserCreationSerializer(
                    instance.user,
                    data=user_data,
                    partial=True,
                    context=self.context  # Passe le contexte (important pour les SerializerMethodField)
                )
                user_serializer.is_valid(raise_exception=True)
                user_serializer.save()
                
        return instance        
    