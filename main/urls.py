from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.generic import *
from django.contrib import admin
from django.urls import include, path
from ajouter.views import *
from dashboard.views import dashboard, maStructure, monPartenaire, user_partenaire, user_structure
from .views import index, recherche, false
from profil.views import UserEditView, profils
from partner.views import Partenaire, Structure, PartenaireOption
from structure.views import detail, Options
from main import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path("rajouter/structure",rajoutstructure , name='rajoutstructure'),
    path("rajouter/structure",rajoutstructureValider, name='rajoutstructureValider'),
    path("rajouter/partenaire",rajoutpartenaire, name='rajoutpartenaire'),
    path("rajouter/profils",rajoutprofils , name='rajoutprofils'),
    path("rajouter/option",rajoutOption, name ='rajoutoption'),
    path("", index, name='index'), 
    path("dash/", dashboard, name='dashboard'),
    path("dash/structure/", maStructure, name='maStructure'),
    path("dash/partenaire/", monPartenaire, name='monPartenaire'),
    path("dash/modifstructure/<int:pk>", user_structure, name='modifstructure'),
    path("dash/modifpartenaire/<str:slug>", user_partenaire, name='modifpartenaire'),
    path("false/", false, name="false"),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('profils/', profils, name="profils" ) , 
    path('profils/modifier', UserEditView.as_view(), name='modifprofils' ) ,
    path('partenaire/', Partenaire, name="partenaire"),
    path('partenaire/option/<int:pk>', PartenaireOption, name="optionbase"),
    path('partenaire/<str:slug>', Structure, name='structure'),
    path('recherche/', recherche, name="recherche"),
    path('detail/<int:pk>', detail, name="detail"),
    path('responsable/<int:pk>', Options, name="responsable"),
    path('activate/<uidb64>/<token>', activate, name="activate"),
    path('listOption/', listeOption, name="listeOption"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpatterns = [
    path('check_username/', check_username, name='check-username'),
    path('check_email/', check_email, name='check-email'),
    path('check_tel/',check_tel, name='check_tel'),
    path('check_nameStructure/',check_nameStruture, name='nameStructure'),
    path('check_password/',check_password, name='check_password'),
    path('check_villePartenaire/', check_villePartenaire, name="check_villePartenaire"),
    path('check_slug/', check_slug, name="check_slug"),
]

urlpatterns += htmx_urlpatterns