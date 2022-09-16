from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .forms import *
from django.urls import reverse_lazy

from django.shortcuts import render


def dashboard(request):
    return render(request,'dashbord.html')

def maStructure(request):
    return render(request,'mastructure.html')

def monPartenaire(request):
    return render(request, 'monpartenaire.html')

class UserEditView(SuccessMessageMixin,generic.UpdateView):
    form_class = ModifPartenaire
    template_name = 'modifpartenaire.html'
    sucess_message = 'Votre profils a bien été modifier'
    
    def get_object(self):
        return self.request.user