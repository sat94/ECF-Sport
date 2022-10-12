from django.shortcuts import redirect, render
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.urls import reverse_lazy


def login(request):    
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('index')

class PasswordsChangeView(PasswordChangeView):
    success_url: reverse_lazy('profils')
    
