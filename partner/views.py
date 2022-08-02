from django.shortcuts import render
from accounts.models import partenaire, structure
from django.core.paginator import Paginator


def Partenaire(request, *arg, **kwargs):
    partenaires = partenaire.objects.all()
    paginator = Paginator(partenaires, 3)
    page = request.GET.get('page')
    pagebjet = paginator.get_page(page)
    context= {"partenaires" : pagebjet}  
    return render(request, "partner.html",context)

def Structure(request, slug):
    structures = structure.objects.filter(slug__iexact= slug)
    paginator = Paginator(structures, 3)
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page)   
    context= {
        "structures" : pagebjets,
        "slug" : slug         
    }
    return render(request, "structure.html",context)







    
