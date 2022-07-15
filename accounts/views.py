from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate


def login(request):    
    return render(request, "login.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')        
    

def logout_user(request):
    logout(request)
    return redirect('index')


 