from django import forms


class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=10)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    nom = forms.CharField(max_length=10)
    prenom = forms.CharField(max_length=10)
    adresse = forms.CharField(max_length=200)
    email = forms.EmailField()
    photo = forms.ImageField()
    cgu_accept = forms.BooleanField()

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de lèttres spéciaux")
        return pseudo
    
    def clean_nom(self):
        nom = self.cleaned_data.get("nom")
        if "$" in nom:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de lèttres spéciaux")
        return nom
    
    def clean_prenom(self):
        prenom = self.cleaned_data.get("prenom")
        if "$" in prenom:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de lèttres spéciaux")
        return prenom
    
    def clean_adresse(self):
        adresse = self.cleaned_data.get("adresse")
        if "$" in adresse:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de lèttres spéciaux")
        return adresse
   


        
    


