from accounts.models import partenaire
from django.contrib.auth.forms import UserChangeForm
from django import forms

class ModifPartenaire(UserChangeForm):    
    class Meta:
        model = partenaire 
        fields = (
            "ville",           
            "description",
            "numberPhone",
            "resp",
            "photo",            
        )
        labels = {
            "numberPhone": "Téléphone",
            "resp" : "Le responsable du partenaire",
       }
        widgets = {
            "description": forms.Textarea(
                attrs={
                    'placeholder':"Vous pouvez rentrer jusqu'à 70 caractères.",
                    'rows' : 5,
                    'cols' : 35,
                }
            ),          
        }  
    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if ".txt" in photo:
            raise forms.ValidationError
        return photo
