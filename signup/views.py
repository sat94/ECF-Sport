from django.http import HttpResponse
from django.shortcuts import render
from signup.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci de vous êtes inscrit au site.")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})
