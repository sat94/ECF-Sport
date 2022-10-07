from django import forms
from accounts.models import partenaire


class Option_par_id(forms.ModelForm):
      class Meta:
        model = partenaire 
        fields = {
            "option",
            "actif"
        }
        widgets = {
             "option": forms.CheckboxSelectMultiple(),
             "actif": forms.CheckboxInput(),
        }
