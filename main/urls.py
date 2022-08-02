from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ajouter.views import Rajout
from .views import index, recherche
from profil.views import profils
from partner.views import Partenaire, Structure
from accounts.views import signup
from structure.views import detail, option
from main import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("rajouter/", Rajout, name='rajouter'),
    path("", index, name='index'), 
    path('accounts/', include('django.contrib.auth.urls')),     
    path('profils/', profils, name="profils" ) , 
    path('partenaire/', Partenaire, name="partenaire"),
    path('compte/', signup, name='signup'),
    path('partenaire/<str:slug>', Structure, name='structure'),
    path('recherche/', recherche, name="recherche"),
    path('detail/<int:pk>', detail,name="detail"),
    path('responsable/<int:pk>', option, name="responsable"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
