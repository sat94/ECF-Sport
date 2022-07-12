from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'), 
    path('login', include("accounts.urls"), name="login"),
    path('signup', include("signup.urls"), name="signup"),      
]
