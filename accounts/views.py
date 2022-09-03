from django.shortcuts import redirect, render
from django.contrib.auth import logout


def login(request):    
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('index')


    
