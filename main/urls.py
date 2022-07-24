from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import index, recherche
from profil.views import profils
from partner.views import Partenaire, start, Structure
from accounts.views import signup
from main import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'), 
    path('accounts/', include('django.contrib.auth.urls')),     
    path('profils/', profils, name="profils" ) , 
    path('partenaire/', Partenaire, name="partenaire"),
    path('starter/', start, name='start'),
    path('compte/', signup, name='signup'),
    path('partenaire/structure/<str:slug>', Structure, name='structure'),
    path('recherche/', recherche, name="recherche"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
