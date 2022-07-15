from django.shortcuts import render


def profils(request):
    return render(request, 'profils.html')