from django.shortcuts import render
from accounts.models import structure, option

def detail(request, pk):
    structures = structure.objects.get(id=pk)
    options = option.objects.all()
    context = {
        "structure" : structures,
        "otpions" : options
    }
    return render(request, "detail.html", context)
    

def Options(request, pk):
    structures = structure.objects.get(id=pk)
    context= {
        "structure" : structures
    }
    return render(request, "option.html", context)


