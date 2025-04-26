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