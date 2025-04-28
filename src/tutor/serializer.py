from rest_framework import serializers
from tutor.models import Tutors
from user.serializer import UserCreationSerializer

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

from django.db import transaction

#Celui ci c'est pour la creation la suppression et la vu hein
class TutorCreationSerializer(serializers.ModelSerializer):
    user = UserCreationSerializer()
    class Meta:
        model = Tutors
        fields = ['user','phone_number','student']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'tutor'
        user_serializer = UserCreationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        tutor = Tutors(user=None,**validated_data)
        try:
            tutor.full_clean(exclude=['user'])
        except DjangoValidationError as e:
            raise DRFValidationError(e.message_dict)
        
        with transaction.atomic():
            user = user_serializer.save()
            tutor.user = user
            tutor.save()
            
        return tutor
    
    from django.db import transaction

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        
        with transaction.atomic():
            # Mise à jour du Tuteur
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