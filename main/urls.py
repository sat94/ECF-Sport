from xml.dom.minidom import Document
from xml.etree.ElementInclude import include

from django.conf.urls.static import static
from django.contrib import admin
from django.forms import Media
from django.urls import path
from .views import index
from accounts.views import login
from signup.views import signup
from main import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'), 
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
