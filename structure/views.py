from django.shortcuts import render
from accounts.models import partenaire, structure, option
from django.contrib.auth.decorators import login_required

@login_required
def details(request, pk):
    structures = structure.objects.get(id=pk)    
    options = option.objects.all().order_by()
    partenaires = partenaire.objects.get(id=structures.part.id)
    listoptionpartenaire = [option_partenaire.id for option_partenaire  in partenaires.option.all()]
    listoptionstructure = [option_structure.id for option_structure  in structures.option.all()] 
    options = option.objects.all()      
    context = {
        "structure" : structures,
        "options" : options, 
        "listoptionpartenaire" : listoptionpartenaire,
        "listoptionstructure" : listoptionstructure     
    }
    return render(request, "detail.html", context)
    
@login_required
def Options(request, pk):
    structures = structure.objects.get(id=pk)
    context= {
        "structure" : structures
    }
    return render(request, "option.html", context)




