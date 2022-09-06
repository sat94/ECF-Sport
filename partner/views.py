from django.shortcuts import render
from accounts.models import option, partenaire, structure
from django.core.paginator import Paginator


def Partenaire(request):
    partenaires = partenaire.objects.all()  
    paginator = Paginator(partenaires, 3)
    page = request.GET.get('page')
    pagebjet = paginator.get_page(page)
    context= {
        "partenaires" : pagebjet,
              
        }  
    return render(request, "partner.html",context)

def Structure(request, slug):
    structures = structure.objects.filter(slug__iexact= slug)
    paginator = Paginator(structures, 3)
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page)   
    context= {
        "structures" : pagebjets,                   
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

def OptionTrue(request,pk):
    pass





    
