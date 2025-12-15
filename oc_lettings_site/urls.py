"""
Module urls.py de la partie accueil du site

Ce module définit les chemins d'accès de chaque partie du site.
- la page d'accueil
- les sous-applications lettings et profiles
- l'administration Django
- une route volontaire en erreur pour tester l'affichage de la page 500

Ce module configure aussi les handlers pour les erreurs 404 et 500
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from . import views

# '', views.index, name='index'
#         --> Page d'accueil du site
# "lettings/", include("lettings.urls")
#         --> Oriente vers la partie lettings
# 'profiles/', include("profiles.urls")
#         --> Oriente vers la partie profiles
# 'admin/', admin.site.urls
#         --> Page administration du site
# 'crash/', views.crash_erreur_500
#         --> Page d'erreur volontaire pour l'affichage de la page 500
urlpatterns = [
    path('', views.index, name='index'),
    path("lettings/", include("lettings.urls")),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('crash/', views.crash_erreur_500),
]


def erreur404_page_non_trouve(request, exception):
    """
    Orientation en cas d'erreur 404 généré par l'utilisateur

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur
        exception (Exception) : Exception remontée lors de la recherche du chemin

    Returns:
        HttpResponse: Réponse contenant le rendu du template "erreurs/404.html"

    """
    return render(request, "erreurs/404.html", status=404)


def erreur500_erreur_serveur(request):
    """
    Orientation en cas d'erreur 500 généré lors de l'utilisation

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur

    Returns:
        HttpResponse: Réponse contenant le rendu du template "erreurs/500.html"

    """
    return render(request, "erreurs/500.html", status=500)


# Déclaration des différents handlers d'erreurs
handler404 = "oc_lettings_site.urls.erreur404_page_non_trouve"
handler500 = "oc_lettings_site.urls.erreur500_erreur_serveur"
