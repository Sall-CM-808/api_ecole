from rest_framework import serializers
from manager.models import SchoolManagers
from user.serializer import UserCreationSerializer

from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError

from django.db import transaction

class SchoolManagerCreationSerializer(serializers.ModelSerializer):
    user = UserCreationSerializer()
    class Meta:
        model = SchoolManagers
        fields = ('user','poste','phone_number')
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'admin'
        user_serializer = UserCreationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        
        manager = SchoolManagers(user=None,**validated_data)
        try:
            manager.full_clean(exclude=['user'])
        except DjangoValidationError as e:
            raise DRFValidationError(e.message_dict)
        
        with transaction.atomic():
            user = user_serializer.save()
            manager.user = user
            manager.save()
        
        return manager
    
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
    