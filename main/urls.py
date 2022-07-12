from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .views import index
from accounts.views import login
from signup.views import signup



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'), 
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),      
]
