import os
from django.http import QueryDict
from accounts.models import *
from profil.forms import Profils
from .forms import *
from ajouter.forms import *
from django.shortcuts import render, redirect



def dashboard(request):
    context={}
    partenaires = partenaire.objects.all()
    structures = structure.objects.all()
    personnel = MyUser.objects.all()   
    context= {
        "partenaires" : partenaires,
        "structures" : structures,
        "personnel": personnel,
    }
    return render(request,'dashbord.html', context)

def ma_structure(request):
    return render(request,'mastructure.html')

def mon_partenaire(request):
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

def delete_previous_pictures(previous):
    os.remove(previous)
    return True
  

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

def modifier_option_valide(request, pk):
    options = option.objects.get(id=pk)
    context= { "option" : options }    
    form = AjoutoptionForm(instance=options)
    if request.method == 'GET':
        return render(request, 'dashboard_option.html', context)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = AjoutoptionForm(data, instance=options)
        if form.is_valid():
            form.save()
            redirect('dashboard')
    return redirect('dashboard')
        
#partenaire

def dashboard_partenaire(request):
    partenaires = partenaire.objects.all()
    context= { "partenaires" : partenaires }
    return render(request,'dashboard_partenaire.html', context)

def delete_partenaire(request, pk):
    part = partenaire.objects.get(id=pk)
    default_image_path = part.photo.path
    partenaire.objects.filter(id=pk).delete()
    delete_previous_pictures(default_image_path)   
    partenaires = partenaire.objects.all()
    context= { "partenaires" : partenaires }
    return render(request, 'dashboard_partenaire.html', context)

def modifier_partenaire(request, pk):
    partenaires = partenaire.objects.get(id=pk)
    form = AjoutPartenaireForm(request.POST or None, instance=partenaires)
    return render(request,'modif-partenaire.html',{'partenaires': partenaires, 'form': form})

def modifier_partenaire_valide(request, pk): 
    part = partenaire.objects.get(id=pk)
    default_image_path = part.photo.path
    form = AjoutPartenaireForm(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('dashboard')

def add_partenaire(request):    
    if request.method == "POST":
        form = AjoutPartenaireForm(request.POST,request.FILES)         
        if form.is_valid():                      
            form.save()
            return redirect('dashboard')
        else:
            form = AjoutPartenaireForm() 
    return render(request, "rajoutpartenaire.html",{"form": form})  

#structure#################################################################  

def dashboard_structure(request):
    structures = structure.objects.all()
    context= { "structures" : structures }
    return render(request, 'dashboard_structure.html', context) 

def delete_structure(request, pk):
    part = structure.objects.get(id=pk)
    default_image_path = part.photo.path
    structure.objects.filter(id=pk).delete()
    delete_previous_pictures(default_image_path)   
    structures = structure.objects.all()
    context= { "structures" : structures }
    return render(request, 'dashboard_structure.html', context)

def modifier_structure(request, pk):
    structures = structure.objects.get(id=pk)
    form = AjoutStrutureForm(request.POST or None, instance=structures)
    return render(request,'modif-structure.html',{'structures': structures, 'form': form})

def modifier_structure_valide(request, pk): 
    part = structure.objects.get(id=pk)
    default_image_path = part.photo.path
    form = AjoutStrutureForm(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('dashboard')

def add_structure(request):    
    if request.method == "POST":
        form = AjoutStrutureForm(request.POST,request.FILES)         
        if form.is_valid():                   
            form.save()
            return redirect('dashboard')
        else:
            form = AjoutPartenaireForm() 
    return render(request, "rajoutstructure.html",{"form": form})  


#Personnel################################################################################

def dashboard_personnel(request):
    personnel = MyUser.objects.all()
    context= { "personnel" : personnel }
    return render(request, 'dashboard_personnel.html', context)

def delete_personnel(request, pk):
    part = MyUser.objects.get(id=pk)
    default_image_path = part.photo.path
    MyUser.objects.filter(id=pk).delete()
    delete_previous_pictures(default_image_path)   
    personnel = MyUser.objects.all()
    context= { "personnel" : personnel }
    return render(request, 'dashboard_personnel.html', context)

def modifier_personnel(request, pk):
    personnel = MyUser.objects.get(id=pk)
    form = Profils(request.POST or None, instance=personnel)
    return render(request,'modif-personnel.html',{'personnel': personnel, 'form': form})

def modifier_personnel_valide(request, pk): 
    part = MyUser.objects.get(id=pk)
    default_image_path = part.photo.path
    form = Profils(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('dashboard')

