from django import forms
from accounts.models import MyUser
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "abonnement", "nom","prenom", "email", 'adresse', "photo"]
        labels = {
            "username": "Nom d'utilisateur",
            "nom": " Votre nom",
            "prenom": "Votre prénom",
            "email" : "Votre mail",            
        }    
       
      
     
  
    def clean_nom(self):
        nom = self.cleaned_data.get("nom")
        if "$" in nom:
            raise forms.ValidationError("Le Nom est incorrecte")
        return nom
    
    def clean_prenom(self):
        prenom = self.cleaned_data.get("prenom")
        if "$" in prenom:
            raise forms.ValidationError("Le prénom est incorrecte")
        return prenom
    
    def clean_adresse(self):
        adresse = self.cleaned_data.get("adresse")
        if "$" in adresse:
            raise forms.ValidationError("L'Adresse est incorrecte")
        return adresse
   


        
    


