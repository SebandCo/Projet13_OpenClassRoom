"""
Module tests_views.py de la partie oc_lettings_site

Ce module teste les vues globales
"""

import pytest
from django.urls import reverse
from oc_lettings_site import urls


def test_index(client):
    """
    Vérifie que la vue index fonctionne (statut 200)
    et contient le mot "Welcome"
    """
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content


def test_crash_view(client):
    """
    Vérifie qu'une exception est levé et que la vue crash s'affiche
    """
    with pytest.raises(Exception):
        client.get("/crash/")


def test_erreur404(client):
    """
    Vérifie que la vue n'est pas trouvé (statut 404)
    et contient la phrase "Mauvais chemin O_o"
    """
    response = client.get("/mauvais_chemin/")
    assert response.status_code == 404
    assert b"Mauvais chemin O_o" in response.content


def test_erreur500(client):
    """
    Appel de la vue 500
    et contient la phrase "Erreur interne du serveur"
    """
    response = urls.erreur500_erreur_serveur(None)
    assert response.status_code == 500
    assert b"Erreur interne du serveur" in response.content
