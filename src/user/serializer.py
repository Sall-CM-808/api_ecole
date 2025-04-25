from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_of_birth','address','profile_picture','role')
    
    #Definition de la fonction qui geneera un mot de pass pour l'utilisateur lors de la creation de son compte
    def generate_password(password_size):
        import string
        import secrets
        safe_punctuation = "!@#$%&*+-=?"
        chars = string.ascii_letters + string.digits + safe_punctuation
        return "".join(secrets.choice(chars) for _ in range(password_size))

    print(generate_password(15))
        
    def create(self, validated_data):
        #Avec ca on recupere les attributs des la class user le password y compris
        password = self.initial_data.get('password',"hadi")
        new_pass = validated_data['password'] = make_password(password)
        print("**********************************************************")
        print(f"Mot de pass non hashé : {password}")
        print(f"Le mot de pass hashé  : {new_pass}")
        print("**********************************************************")
        return super().create(validated_data)
    
