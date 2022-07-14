from django.shortcuts import redirect, render
from signup.forms import SignupForm




def signup(request):
    context = {}
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)         
        if form.is_valid():
            form.save()
          
            return redirect('index')
        else:
            context["errors"] = form.errors
    form = SignupForm()
    context["form"]= form

    return render(request, "signup.html", context= context)
