from django.shortcuts import redirect, render
from accounts.models import partenaire
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

def recherche(request):
     return render(request, 'recherche.html')
    