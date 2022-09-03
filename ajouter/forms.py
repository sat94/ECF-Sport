from accounts.models import MyUser, option, partenaire, structure
from django.contrib.auth.forms import UserCreationForm

from django import forms

class AjoutoptionForm(forms.ModelForm):
    class Meta:
        model = option
        fields = "__all__"
        labels = {
            "slug" : "Titre",          
        }   
        widgets = {
            "description": forms.Textarea(
                 attrs={
                    'placeholder':"Vous pouvez rentrer jusqu'à 90 caractères.",
                    'rows' : 6,
                    'cols' : 40,
                }
            )
        }     

class SignupForm(UserCreationForm):
    username = forms.CharField(label="nom d'utilisateur") 
    class Meta:
        model = MyUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
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
            "Groupe" : "Permission",
        }  
        widgets = {
            "password" : forms.PasswordInput(),
        } 
   
    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if ".txt" in photo:
            raise forms.ValidationError
        return photo       

class AjoutStrutureForm(forms.ModelForm): 
    class Meta:
        model = structure
        fields = [
            "nom",           
            "adresse",
            "membre",
            "numberPhone",          
            "option",           
            "part",             
            "user",
            "photo",
            "piscine", 
            "haman",
            "sauna",                                    
        ]
        labels = {
            "user" : "le responsable de la structure (facultatif)",
            "slug": "Ville de la structure",
            "part": "Appartiens au partenaire (facultatif)",
            "nom": "Nom de la structure",
            "adresse": "Adresse",
            "numberPhone": "Téléphone",  
            "membre"  : "Nombre de membres",                
        }
        widgets = {
            "option": forms.CheckboxSelectMultiple(),
            "adresse": forms.Textarea(attrs={"rows" : 2, "cols": 23}),
        }  
       
    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if ".txt" in photo:
            raise forms.ValidationError
        return photo 
 
class AjoutPartenaireForm(forms.ModelForm):    
    class Meta:
        model = partenaire 
        fields = (
            "ville",           
            "description",
            "numberPhone",
            "resp",
            "photo",
            "option"
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
            "option": forms.CheckboxSelectMultiple(),
        }  
    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if ".txt" in photo:
            raise forms.ValidationError
        return photo

