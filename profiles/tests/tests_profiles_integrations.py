"""
Module tests_integration.py de la partie profiles

Ce module teste différents scénarios
"""
import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_navigation_profiles_detail_lettings(client):
    """
    Vérifie que le passage d'une page profiles à une page index lettings fonctionne
    """
    user = User.objects.create_user(username="harry", password="secret")
    Profile.objects.create(user=user, favorite_city="Poudlard")

    # 1er étape : affichage de la page profil
    url = reverse("profiles:profile", args=[user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert b"harry" in response.content
    assert b"Poudlard" in response.content

    # 2eme étape : lien vers lettings
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content


@pytest.mark.django_db
def test_navigation_profiles_detail_accueil(client):
    """
    Vérifie que le passage d'une page profiles à la page d'accueil fonctionne
    """
    user = User.objects.create_user(username="harry", password="secret")
    Profile.objects.create(user=user, favorite_city="Poudlard")

    # 1er étape : affichage de la page profil
    url = reverse("profiles:profile", args=[user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert b"harry" in response.content
    assert b"Poudlard" in response.content

    # 2eme étape : lien vers l'acceuil
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content


@pytest.mark.django_db
def test_navigation_profiles_index_lettings(client):
    """
    Vérifie que le passage d'une page index profiles à une page index lettings fonctionne
    """
    # 1er étape : affichage de la page profil
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Profiles" in response.content

    # 2eme étape : lien vers lettings
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content


@pytest.mark.django_db
def test_navigation_profiles_index_accueil(client):
    """
    Vérifie que le passage d'une page index profiles à la page d'accueil fonctionne
    """
    # 1er étape : affichage de la page profil
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Profiles" in response.content

    # 2eme étape : lien vers l'acceuil
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content


@pytest.mark.django_db
def test_navigation_profiles_index_detail(client):
    """
    Vérifie que le passage d'une page index profiles à une page detail profiles fonctionne
    """
    user = User.objects.create_user(username="harry", password="secret")
    Profile.objects.create(user=user, favorite_city="Poudlard")

    # 1er étape : affichage de la page index profiles
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Profiles" in response.content

    # 2eme étape : affichage de la page profil
    url = reverse("profiles:profile", args=[user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert b"harry" in response.content
    assert b"Poudlard" in response.content
