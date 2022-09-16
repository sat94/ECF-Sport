from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .forms import Profils
from django.urls import reverse_lazy



def profils(request):
    return render(request, 'profils.html')


class UserEditView(SuccessMessageMixin,generic.UpdateView):
    form_class = Profils
    template_name = 'modifprofils.html'
    sucess_message = 'Votre profils a bien été modifier'
    
    def get_object(self):
        return self.request.user