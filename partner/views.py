from django.shortcuts import render
from accounts.models import option, partenaire, structure


def Partenaire(request):
    partenaires = partenaire.objects.all()  
    context= {"partenaires" : partenaires}  
    return render(request, "partner.html",context)

def Structure(request, slug):
    structures = structure.objects.filter(slug__iexact= slug)      
    context= {
        "structures" : structures,                   
    }
    return render(request, "structure.html",context)

def PartenaireOption(request, pk):
    structures = structure.objects.filter(part=pk)
    partenaires = partenaire.objects.get(id=pk)
    listoptionid = [option_partenaire.id for option_partenaire  in partenaires.option.all()]
    options = option.objects.all()        
    context= { "partenaires" : partenaires,
               "options" : options,
               "structures": structures,
               "listoptionid" : listoptionid
    }
    return render(request,"optionPartenaire.html",context)





    
