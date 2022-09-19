from accounts.models import MyUser, partenaire, structure
from django.contrib.auth.forms import UserChangeForm
from django import forms

class ModifPartenaire(UserChangeForm):    
    class Meta:
        model = partenaire
        fields = (
            "ville",           
            "description",
            "numberPhone",          
            "photo",            
        )
        labels = {
            "numberPhone": "Téléphone",        
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

class ModifStructureForm(forms.ModelForm): 
    class Meta:
        model = structure
        fields = [
            "nom",           
            "adresse",
            "membre",
            "numberPhone",        
            "photo",
            "piscine", 
            "haman",
            "sauna",                                    
        ]
        labels = {
            "user" : "le responsable de la structure (facultatif)",        
            "nom": "Nom de la structure",
            "adresse": "Adresse",
            "numberPhone": "Téléphone",  
            "membre"  : "Nombre de membres",                
        }
        widgets = {
          
            "adresse": forms.Textarea(attrs={"rows" : 2, "cols": 23}),
        }  
       
    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if ".txt" in photo:
            raise forms.ValidationError
        return photo 

