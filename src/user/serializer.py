from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_of_birth','address','profile_picture','role')
    
    def rand_char(self):
        char = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
        number = [1,2,3,4,5,6,7,8,9]
        special_char = ['&',"'","œ","é","(","-","_","è","ç",""],
    
    
    def create(self, validated_data):
        #Avec ca on recupere les attributs des la class user le password y compris
        password = self.initial_data.get('password',"hadi")
        new_pass = validated_data['password'] = make_password(password)
        print("**********************************************************")
        print(f"Mot de pass non hashé : {password}")
        print(f"Le mot de pass hashé  : {new_pass}")
        print("**********************************************************")
        return super().create(validated_data)
    
