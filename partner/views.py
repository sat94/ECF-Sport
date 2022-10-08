from django.shortcuts import redirect, render
from accounts.models import option, partenaire, structure
from django.contrib.auth.decorators import login_required
from partner.forms import Actif_par_id, Option_par_id
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

@login_required
def Partenaire(request):
    partenaires = partenaire.objects.all()  
    context= {"partenaires" : partenaires}  
    return render(request, "partner.html",context)

@login_required
def Structure(request, slug):
    structures = structure.objects.filter(slug__iexact= slug)      
    context= {
        "structures" : structures,                   
    }
    return render(request, "structure.html",context)


def Partenaire_option(request, pk):
    partenaires = partenaire.objects.get(id=pk)
    listoptionid = [option_partenaire.id for option_partenaire  in partenaires.option.all()]
    form = Option_par_id(instance=partenaires)
    forms = Actif_par_id(instance=partenaires)
    options = option.objects.all()  
    structures = structure.objects.filter(part=pk)
    context= { "partenaires" : partenaires,
               "options" : options,
               "structures": structures,
               "listoptionid" : listoptionid,
               "form": form,
               "forms": forms
    }
    return render(request,"optionPartenaire.html",context)


def option_partenaire_valide(request, pk): 
    partenaires = partenaire.objects.get(id=pk) 
    form = Option_par_id(request.POST, instance=partenaires)         
    if form.is_valid():
        print(vars(form.fields['option']))
        form.save()
        return("index")
    return("index")


    

class partenaireUpdateView(SuccessMessageMixin, UpdateView):
    model = partenaire
    template_name = "optionPartenaire2.html"
    # fields = ['option','actif']
    form_class = Option_par_id
    success_message = "les options ont bien été changer"
    success_url = reverse_lazy('index')
