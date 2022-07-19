from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import index
from profil.views import profils
from partner.views import partenaire
from main import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'), 
    path('accounts/', include('django.contrib.auth.urls'), name='login'),  
    path('profils/', profils, name="profils" ) , 
    path('partenaire/', partenaire, name="partenaire"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
