from django.shortcuts import render
from accounts.models import structure

def detail(request, pk):
    structures = structure.objects.get(id=pk)
    context = {
        "structure" : structures
    }
    return render(request, "detail.html", context)
    

def option(request, pk):
    structures = structure.objects.get(id=pk)
    context= {
        "structure" : structures
    }
    return render(request, "option.html", context)


def option(request, pk):
    structures = structure.objects.get(id=pk)
    context= {
        "structure" : structures
    }
    return render(request, "option.html", context)