from django.shortcuts import render
from accounts.models import partenaire, structure
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
    # tel = structure.numberPhone
    # phone = '-'.join([tel[i:i+2] for i in range(0, len(tel), 2)])
    paginator = Paginator(structures, 3)
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page)   
    context= {
        "structures" : pagebjets, 
        # "phone" : phone,          
    }
    return render(request, "structure.html",context)

def PartenaireOption(request):
    option = partenaire.objects.all()
    context= {
        "option" : option,
    }
    return render(request,"optionPartenaire.html",context)







    
