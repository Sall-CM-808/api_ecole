from rest_framework import serializers
from professor.models import Professors
from user.serializer import UserCreationSerializer
from django.db import transaction
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

#Ce serializer c'est pour la creation,la vue et la suppression. Pas envi de changer son nom hein
class ProfessorCreationSerializer(serializers.ModelSerializer):
    user = UserCreationSerializer()
    class Meta:
        model = Professors
        fields = ('user','subject','level','phone_nuber')
        
    #Maintenant ici on envera chaque donnée ou il faut
    def create(self, validated_data):
        #On recupere les données de l'utilisateur et on les verifie
        user_data = validated_data.pop('user')
        user_data['role'] = 'professor'
        user_serializer = UserCreationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        
        #On fait pareil Pour le professeur
        #   On recupere ces données
        professor = Professors(user=None,**validated_data)
        #On les verifie
        try:
            #On lui dit de ne pas verifier le user car il n'est pas encore enregistré
            professor.full_clean(exclude=['user'])
        except DjangoValidationError as e:
            raise DRFValidationError(e.message_dict)
        
        #Avec ca on s'assure que les deux seront enregistré. Si une rate les autrse aussi
        with transaction.atomic():
            user = user_serializer.save()
            professor.user = user
            professor.save()
        
        return professor
    
    #Maintennat essayons de valider la table professor du genre faire en sorte qu'un mail
    #soit obligatoire pour lui
    def validate(self, data):
        user_data = data.get('user',{})
        email = user_data.get('email')
        if not email:
            raise serializers.ValidationError({
                'user':{'email':"l'adresse email est obligatoire pour un professeur"}
            })
        return data