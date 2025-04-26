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
        fields = ['user','phone_number','student','user']
    
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
        