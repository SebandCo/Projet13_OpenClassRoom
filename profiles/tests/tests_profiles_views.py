"""
Module tests_views.py de la partie profiles

Ce module teste les vues Profiles
"""
import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_index(client):
    """
    Vérifie que la vue profiles:index fonctionne (statut 200)
    et contient le mot "Profiles"
    """
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Profiles" in response.content


@pytest.mark.django_db
def test_profiles_detail(client):
    """
    Vérifie que la vue profiles détails fonctionne (statut 200)
    et contient le titre du Profiles
    """
    user = User.objects.create_user(username="harry", password="secret")
    Profile.objects.create(user=user, favorite_city="Poudlard")

    url = reverse("profiles:profile", args=[user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert b"harry" in response.content
    assert b"Poudlard" in response.content


@pytest.mark.django_db
def test_profiles_detail_ko(client):
    """
    Vérifie que la vue profiles détails renvoie une erreur si non trouvé
    """
    url = reverse("profiles:profile", args=[9999])
    response = client.get(url)
    assert response.status_code == 404
    assert b"Mauvais chemin O_o" in response.content
