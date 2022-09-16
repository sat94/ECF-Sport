from accounts.models import MyUser
from django.contrib.auth.forms import UserChangeForm
from django import forms


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
        
    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if ".txt" in photo:
            raise forms.ValidationError
        return photo       