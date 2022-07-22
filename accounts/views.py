from django.shortcuts import redirect, render
from django.contrib.auth import logout
from accounts.forms import SignupForm
from django.core.mail import send_mail
from main import settings

def login(request):    
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('index')

    
def signup(request):
    context = {}
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)         
        if form.is_valid():
            form.save()
            subject = "Bienvenu sur API-SPORT"
            message = "Bienvenue \n Nous sommes heureux de vous compter parmi nous \n\n\n merci \n L'administrateur"
            from_email = settings.EMAIL_HOST_USER
            to_list = ['sultan77@live.fr']
            send_mail(subject, message, from_email, to_list, fail_silently=False)
        

            return redirect('index')
        else:
            context["errors"] = form.errors
    form = SignupForm()
    context["form"]= form

    return render(request, "signup.html", context= context)