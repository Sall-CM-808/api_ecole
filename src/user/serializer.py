from rest_framework import serializers
from coreApi import settings
from user.models import User
from django.contrib.auth.hashers import make_password
import string
import secrets
from django.core.mail import send_mail


#Definition de la fonction qui geneera un mot de pass pour l'utilisateur lors de la creation de son compte
def generate_password(password_size):
    my_own_punctuation = "!@#$%&*+-=?"
    chars = string.ascii_letters + string.digits + my_own_punctuation
    return "".join(secrets.choice(chars) for _ in range(password_size))


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_of_birth','address','profile_picture','role')
    
        
    def create(self, validated_data):
        #Avec ca on recupere les attributs des la class user le password y compris
        password = self.initial_data.get('password',generate_password(15))
        new_pass = validated_data['password'] = make_password(password)
        print("**********************************************************")
        print(f"Mot de pass non hashé : {password}")
        print(f"Le mot de pass hashé  : {new_pass}")
        print("**********************************************************")
        
        #Là on envoie un mail au user pour lui dire que son compte a été créé et on lui donne meme son mot de pass
        #On lui dit de changer son mot de pass lors de sa premiere connexion
        message = f"""
        Bonjour {validated_data['first_name']} {validated_data['last_name']} L'equipe djangui est heureuse de vous compter
parmi ses membres.\n\n\n 
Dans un souci de securité, nous prions de vous connecter sur votre compte djangui et modifier votre mot de pass
qui vous a été attribué. Pour vous connecter sur votre compte nous vous prions d'entrer votre nom d'utilisateur
et aussi d'entrer ceci comme mot de pass {password}\n\n 
Merci et surtout si vous avez des besoins, nous vous prions de bien vouloir nous contacter sur cette
adresse ou sur la partie contactez-nous de notre platforme et nous nous ferons un immense plaisir de
aider. Merci Albarka WonouWali Iniké. Et pour les autres langues nous y travaillons
        """
        objet = "Bienvenu chez Djangui"
        send_mail(
            subject=objet,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[validated_data['email']],
            fail_silently=False,
        )
        print(message)
        
        return super().create(validated_data)
    
