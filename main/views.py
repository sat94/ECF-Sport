from django.shortcuts import render

from accounts.models import MyUser


def index(request):
    return render(request,'index.html')

def recherche(request):
     return render(request,'recherche.html')
    
def false(request):
    return render(request,"false.html")


