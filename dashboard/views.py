import os
from django.http import QueryDict
from accounts.models import *
from .forms import *
from ajouter.forms import *
from django.shortcuts import render, redirect



def dashboard(request):
    return render(request,'dashbord.html')

def maStructure(request):
    return render(request,'mastructure.html')

def monPartenaire(request):
    return render(request, 'monpartenaire.html')

def user_partenaire(request, slug):
    part = partenaire.objects.get(slug=slug)
    default_image_path = part.photo.path
    form = ModifPartenaire(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('monPartenaire')
    return render(request,'modifpartenaire.html',{'partenaire':part, 'form': form})

def user_structure(request, pk):
    part = structure.objects.get(id=pk)
    default_image_path = part.photo.path
    form = ModifStructureForm(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('maStructure')
    return render(request,'modifstructure.html',{'structure':part, 'form': form})

def delete_previous_picture(previous,new):
    if previous != new:
        os.remove(previous)
        return True
    return False    

def personnel(request):
    return render(request,"personnel.html") 


def dashboard_structure(request):
    structures = structure.objects.all()
    context= { "structure" : structures }
    return render(request, 'dashboard_structure.html', context)

#option

def dashboard_option(request):
    options = option.objects.all()
    context= { "option" : options }
    return render(request, 'dashboard_option.html', context)

def delete_option(request, pk):
    option.objects.filter(id=pk).delete()
    options = option.objects.all()
    context= { "option" : options }
    return render(request, 'dashboard_option.html', context)

def modifier_option(request, pk):
    options = option.objects.get(id=pk)
    form = AjoutoptionForm(request.POST or None, instance=options)
    return render(request,'modif-option.html',{'option': options, 'form': form})

def modifier_optionvalide(request, pk):
    options = option.objects.get(id=pk)
    context= { "option" : options }    
    form = AjoutoptionForm(instance=options)
    if request.method == 'GET':
        return render(request, 'dashboard_option.html', context)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        print(request.body)
        form = AjoutoptionForm(data, instance=options)
        if form.is_valid:
            form.save()
            redirect('dashboard_option')
        
#partenaire

def dashboard_partenaire(request):
    partenaires = partenaire.objects.all()
    context= { "partenaires" : partenaires }
    return render(request,'dashboard_partenaire.html', context)

def delete_partenaire(request, pk):
    partenaire.objects.filter(id=pk).delete()
    partenaires = partenaire.objects.all()
    context= { "partenaires" : partenaires }
    return render(request, 'dashboard_partenaire.html', context)

def delete_structure(request, pk):
    structure.objects.filter(id=pk).delete()
    structures = structure.objects.all()
    context= { "structure" : structures }
    return render(request, 'dashboard_structure.html', context)

def delete_user(request, pk):
    MyUser.objects.filter(id=pk).delete()
    User = MyUser.objects.all()
    context= { "username" : User }
    return render(request, 'personnel.html', context)