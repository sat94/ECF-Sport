from accounts.models import MyUser
from django.contrib.auth.forms import UserChangeForm


class Profils(UserChangeForm):
    password = None
    class Meta:
        model = MyUser
        fields = [
            "username",
            "nom", 
            "prenom",               
            "adresse", 
            "CodePostal", 
            "ville",
            "photo",
            "permission",                
            ]
        labels = {
            "username": "Nom d'utilisateur",
            "nom": " Votre nom",
            "prenom": "Votre prénom",
            "email" : "Votre mail",  
            "CodePostal" : "Votre code Postale",
            "ville" : "Votre ville",          
            "photo" : "Votre photo (facultatif)",         
        }  
      
       
    
