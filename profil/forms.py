from accounts.models import MyUser
from django.contrib.auth.forms import UserChangeForm
from django import forms
import os


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
            "part",  
            "entreprise",       
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
    
    def save(self, commit=True):
        if self.instance.photo.path != self.initial['photo'].path:
            os.remove(self.initial['photo'].path)
        return super().save(commit)
