"""
Module tests_urls.py de la partie oc_lettings_site

Ce module teste les urls globales du projet
"""

from django.urls import reverse, resolve
from oc_lettings_site import views
from oc_lettings_site import urls


def test_index_url_resolves():
    """
    Vérifie que l'URL index dirige bien vers la vue correspondante
    """
    url = reverse("index")
    assert resolve(url).func == views.index


def test_crash_url_resolves():
    """
    Vérifie que l'URL crash dirige bien vers la vue correspondante
    """
    url = "/crash/"
    assert resolve(url).func == views.crash_erreur_500


def test_handlers():
    """
    Vérifie que les urls spécifique d'erreur dirigent bien vers les vues correspondantes
    """
    assert urls.handler404 == "oc_lettings_site.urls.erreur404_page_non_trouve"
    assert urls.handler500 == "oc_lettings_site.urls.erreur500_erreur_serveur"
