from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("lettings/", include("lettings.urls")),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('crash/', views.crash_erreur_500),
]


def erreur404_page_non_trouve(request, exception):
    return render(request, "erreurs/404.html", status=404)


def erreur500_erreur_serveur(request):
    return render(request, "erreurs/500.html", status=500)


handler404 = "oc_lettings_site.urls.erreur404_page_non_trouve"
handler500 = "oc_lettings_site.urls.erreur500_erreur_serveur"
