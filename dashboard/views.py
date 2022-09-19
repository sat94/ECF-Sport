import os
from accounts.models import structure
from .forms import *
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
    return render(request,'modifpartenaire.html',{'partenaire':part,
                                                  'form': form})


def user_structure(request, pk):
    part = structure.objects.get(id=pk)
    default_image_path = part.photo.path
    form = ModifStructureForm(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('maStructure')
    return render(request,'modifstructure.html',{'structure':part,
                                                  'form': form})

def delete_previous_picture(previous,new):
    if previous != new:
        os.remove(previous)
        return True
    return False     