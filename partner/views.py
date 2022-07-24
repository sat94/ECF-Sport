from django.shortcuts import get_object_or_404, redirect, render
from pytest import param
from accounts.models import partenaire, structure, MyUser
from partner.forms import starter
from django.core.paginator import Paginator

def Partenaire(request, *arg, **kwargs):
    partenaires = partenaire.objects.all()
    paginator = Paginator(partenaires, 3)
    page = request.GET.get('page')
    pagebjet = paginator.get_page(page)
    context= {
        "partenaires" : pagebjet,
        
    }
    return render(request, "partner.html",context)

def slug():
    model = partenaire
    slug = model.slug
    return slug


def Structure(request, slug):
    structures = structure.objects.filter(slug__iexact= slug)
    post = structures
    paginator = Paginator(structures, 3)
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page)   
    context= {
        "structures" : pagebjets,
        "post" : post,
    }
    return render(request, "structure.html",context)




def start(request):
    context = {}
    if request.method == "POST":
        form = starter(request.POST, request.FILES)         
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context["errors"] = form.errors
    form = starter()
    context["form"]= form

    return render(request, "start.html", context= context)


    
