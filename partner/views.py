from django.shortcuts import render


def partenaire(request):
    return render(request, "partner.html")
    