"""
Module tests_integration.py de la partie lettings

Ce module teste différents scénarios
"""
import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_navigation_lettings_detail_profiles(client):
    """
    Vérifie que le passage d'une page lettings à une page index profiles fonctionne
    """
    address = Address.objects.create(
        number=4, street="Privet Drive", city="Little Whinging",
        state="UK", zip_code="12345", country_iso_code="ANG"
    )
    letting = Letting.objects.create(
        title="Famille Dursley", address=address
    )

    # 1er étape : affichage de la page location
    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Famille Dursley" in response.content

    # 2eme étape : lien vers profiles
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Profiles" in response.content


@pytest.mark.django_db
def test_navigation_lettings_detail_accueil(client):
    """
    Vérifie que le passage d'une page lettings à la page d'accueil fonctionne
    """
    address = Address.objects.create(
        number=4, street="Privet Drive", city="Little Whinging",
        state="UK", zip_code="12345", country_iso_code="ANG"
    )
    letting = Letting.objects.create(
        title="Famille Dursley", address=address
    )

    # 1er étape : affichage de la page location
    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Famille Dursley" in response.content

    # 2eme étape : lien vers l'acceuil
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content


@pytest.mark.django_db
def test_navigation_lettings_index_profiles(client):
    """
    Vérifie que le passage d'une page index lettings à une page index profiles fonctionne
    """
    # 1er étape : affichage de la page location
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content

    # 2eme étape : lien vers profiles
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Profiles" in response.content


@pytest.mark.django_db
def test_navigation_lettings_index_accueil(client):
    """
    Vérifie que le passage d'une page index lettings à la page d'accueil fonctionne
    """
    # 1er étape : affichage de la page location
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content

    # 2eme étape : lien vers l'acceuil
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content


@pytest.mark.django_db
def test_navigation_lettings_index_detail(client):
    """
    Vérifie que le passage d'une page index lettings à une page detail lettings fonctionne
    """
    address = Address.objects.create(
        number=4, street="Privet Drive", city="Little Whinging",
        state="UK", zip_code="12345", country_iso_code="ANG"
    )
    letting = Letting.objects.create(
        title="Famille Dursley", address=address
    )

    # 1er étape : affichage de la page index lettings
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content

    # 2eme étape : lien vers la page profil
    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Famille Dursley" in response.content
