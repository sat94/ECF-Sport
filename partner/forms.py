from django import forms

from accounts.models import partenaire
class starter(forms.ModelForm):
    
    class Meta:
        model = partenaire
        fields = [ "ville", "email"]
        labels = {
            "ville": "Rajouter la ville du Partenaire",
            "email" : "Votre mail",  
             
        }



