from accounts.models import MyUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [ "username", "nom", "prenom", "email", "adresse", "CodePostal", "ville", "photo", "is_admin"]
        labels = {
            "username": "Nom d'utilisateur",
            "nom": " Votre nom",
            "prenom": "Votre prénom",
            "email" : "Votre mail",  
            "CodePostal" : "Votre code Postale",
            "ville" : "Votre ville",
            "is_admin" : "Administrateur"
        }    
       