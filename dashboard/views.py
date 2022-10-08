import os
from django.http import QueryDict
from accounts.models import *
from django.views.decorators.clickjacking import xframe_options_exempt
from profil.forms import Profils
from .forms import *
from ajouter.forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import  pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.http.response import JsonResponse


@login_required
def dashboard(request):
    context={}
    partenaires = partenaire.objects.all()
    part_count = partenaires.count()
    structures = structure.objects.all()
    struct = structures.count()
    personnel = MyUser.objects.all()  
    per = personnel.count() 
    qs = structures
    project = [
        {
            'Structure': x.nom,
            'Nombre': x.membre,           
            'Responsable' : x.nom
        } for x in qs
    ]
    df = pd.DataFrame(project)    
    fig = px.bar(df, x ="Structure", y="Nombre" , color="Responsable", width=450, height=400)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.layout.legend = {'font_color':'white'}
    fig.update_xaxes({'color':'white'})
    fig.update_yaxes({'color':'white'})
  
    gantt_plot = plot(fig, output_type="div")

    cam=[{
        "nom" : x.nom,
        "membre"  : x.membre, 
        "Partenaire" : x.nom,        
    } for x in qs
    ]

    df = pd.DataFrame(cam)  
    figa = px.pie(df, values='membre',names="nom", title ="Api-Sport", color="Partenaire", width=450, height=400)
    figa.layout.paper_bgcolor = 'black'
    figa.layout.legend = {'font_color':'white'}
    figa.update_layout(title_font_color='white')
    figa.update_xaxes({'color':'white'})
    figa.update_yaxes({'color':'white'})
    cam_plot= plot(figa, auto_open=False, output_type="div")
          
    context= {
        "partenaires" : partenaires,
        "part" : part_count,
        "structures" : structures,
        "struct": struct,
        "personnel": personnel,
        "per": per, 
        "graph" : gantt_plot,  
        "cam" : cam_plot,
    }
    return render(request,'dashbord.html', context)

@login_required
def ma_structure(request):
    return render(request,'mastructure.html')

@login_required
def mon_partenaire(request):
    return render(request, 'monpartenaire.html')

@login_required
def user_partenaire(request, slug):
    part = partenaire.objects.get(slug=slug)
    if MyUser.photo:
        default_image_path = part.photo.path
    form = ModifPartenaire(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('monPartenaire')
    return render(request,'modifpartenaire.html',{'partenaire':part, 'form': form})

@login_required
def user_structure(request, pk):
    part = structure.objects.get(id=pk)
    if structure.photo:
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

@login_required
def delete_previous_pictures(previous):
    os.remove(previous)
    return True  

#option

@login_required
def dashboard_option(request):
    options = option.objects.all()
    context= { "option" : options }
    return render(request, 'dashboard_option.html', context)

@login_required
def delete_option(request, pk):
    option.objects.filter(id=pk).delete()
    options = option.objects.all()
    context= { "option" : options }
    return render(request, 'dashboard_option.html', context)

@login_required
def modifier_option(request, pk):
    options = option.objects.get(id=pk)
    form = AjoutoptionForm(request.POST or None, instance=options)
    return render(request,'modif-option.html',{'option': options, 'form': form})

@login_required
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
        
#partenaire#############################################################################

@login_required
def dashboard_partenaire(request):
    partenaires = partenaire.objects.all()
    form = valid_par_id()
    context= { "partenaires" : partenaires,
                "form" : form
    }
    return render(request,'dashboard_partenaire.html', context)

@login_required
def delete_partenaire(request, pk):
    part = partenaire.objects.get(id=pk)
    if part.photo:
        default_image_path = part.photo.path
    partenaire.objects.filter(id=pk).delete()
    if default_image_path:
        delete_previous_pictures(default_image_path)   
    partenaires = partenaire.objects.all()
    context= { "partenaires" : partenaires }
    return render(request, 'dashboard_partenaire.html', context)

@login_required
def modifier_partenaire(request, pk):
    partenaires = partenaire.objects.get(id=pk)
    form = AjoutPartenaireForm(instance=partenaires)
    return render(request,'modif-partenaire.html',{'partenaires': partenaires, 'form': form})

@login_required
def modifier_partenaire_valide(request, pk): 
    part = partenaire.objects.get(id=pk)
    if part.photo:
        default_image_path = part.photo.path
    form = AjoutPartenaireForm(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('dashboard')

@login_required
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

@login_required
def dashboard_structure(request):
    structures = structure.objects.all()
    context= { "structures" : structures }
    return render(request, 'dashboard_structure.html', context) 

@login_required
def delete_structure(request, pk):
    part = structure.objects.get(id=pk)
    if part.photo:
        default_image_path = part.photo.path
    structure.objects.filter(id=pk).delete()
    if part.photo:
        delete_previous_pictures(default_image_path)   
    structures = structure.objects.all()
    context= { "structures" : structures }
    return render(request, 'dashboard_structure.html', context)

@login_required
def modifier_structure(request, pk):
    structures = structure.objects.get(id=pk)
    form = AjoutStrutureForm(request.POST or None, instance=structures)
    return render(request,'modif-structure.html',{'structures': structures, 'form': form})

@login_required
def modifier_structure_valide(request, pk): 
    part = structure.objects.get(id=pk)
    if part.photo:
        default_image_path = part.photo.path
    form = AjoutStrutureForm(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
           delete_previous_picture(default_image_path, part.photo.path)
        form.save()
        return redirect('dashboard')

@login_required
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

@login_required
def dashboard_personnel(request):
    personnel = MyUser.objects.all()
    context = { "personnel" : personnel }
    return render(request, 'dashboard_personnel.html', context)

@login_required
def delete_personnel(request, pk):
    part = MyUser.objects.get(id=pk)
    if part.photo:
        default_image_path = part.photo.path
    MyUser.objects.filter(id=pk).delete()
    if default_image_path:
        delete_previous_pictures(default_image_path)   
    personnel = MyUser.objects.all()
    context= { "personnel" : personnel }
    return render(request, 'dashboard_personnel.html', context)

@login_required
def modifier_personnel(request, pk):
    personnel = MyUser.objects.get(id=pk)
    form = Profils(request.POST or None, instance=personnel)
    return render(request,'modif-personnel.html',{'personnel': personnel, 'form': form})

@login_required
def modifier_personnel_valide(request, pk): 
    part = MyUser.objects.get(id=pk)
    default_image_path =  None
    if  part.photo:
        default_image_path = part.photo.path
    form = Profils(request.POST or None, request.FILES or None, instance=part)
    if form.is_valid():
        if len(request.FILES)!= 0:
            if default_image_path:
                delete_previous_picture(default_image_path, part.photo.path)
        form.save()
    return redirect('dashboard')

def valid_partenaire_valide(request, pk): 
    partenaires = partenaire.objects.get(id=pk) 
    form = valid_par_id(request.POST, instance=partenaires)         
    if form.is_valid():
        form.save()
        return JsonResponse(form)  # No need to use json.dumps()
    return("index")
