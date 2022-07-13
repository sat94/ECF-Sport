from django.shortcuts import render
from signup.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILE)         
        if form.is_valid():
            image = request.FILES['image']
            form = SignupForm()
            context = {'form': form, 'image': image}
            return render(request, 'web_ui/home.html', context)
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})
