from accounts.models import partenaire, structure
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

class ModifStructureForm(UserChangeForm): 
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
       

class valid_par_id(UserChangeForm):
      class Meta:
        model = partenaire 
        fields = {
            "actif"
        }
        widgets = {            
             "actif": forms.CheckboxInput(),
        }
