"""
Module tests_integration.py de la partie oc_lettings_site

Ce module teste différents scénarios
"""
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_navigation_accueil_profiles(client):
    """
    Vérifie que le passage de la page d'accueil vers la page index profiles fonctionne
    """
    # 1er étape : affichage de la page d'accueil
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content

    # 2eme étape : lien vers profiles
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Profiles" in response.content


@pytest.mark.django_db
def test_navigation_accueil_lettings(client):
    """
    Vérifie que le passage de la page d'accueil vers la page index lettings fonctionne
    """
    # 1er étape : affichage de la page d'accueil
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content

    # 2eme étape : lien vers lettings
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content
