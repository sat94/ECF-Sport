from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from .forms import Profils



def profils(request):
    return render(request, 'profils.html')


class UserEditView(UpdateView,SuccessMessageMixin):
    form_class = Profils
    template_name = 'modifprofils.html'
    sucess_message = 'Votre profils a bien été modifier'
    
    def get_object(self):
        return self.request.user
