from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView

from accounts.models import MyUser
from .forms import Profils
#from dashboard.views import d
from django.urls import reverse_lazy



def profils(request):
    return render(request, 'profils.html')


class UserEditView(UpdateView,SuccessMessageMixin):
    form_class = Profils
    #default_image_path = MyUser.photo.path
    template_name = 'modifprofils.html'
    sucess_message = 'Votre profils a bien été modifier'
    
    def get_object(self):
        return self.request.user
