from django import forms
from accounts.models import partenaire


class Option_par_id(forms.ModelForm):
      class Meta:
        model = partenaire 
        fields = {
            "option",            
        }
        widgets = {
             "option": forms.CheckboxSelectMultiple(),             
        }

class Actif_par_id(forms.ModelForm):
      class Meta:
        model = partenaire 
        fields = {            
            "actif"
        }
        widgets = {            
             "actif": forms.CheckboxInput(),
        }
