"""
Module tests_views.py de la partie lettings

Ce module teste les vues Address et Letting
"""
import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index(client):
    """
    Vérifie que la vue lettings:index fonctionne (statut 200)
    et contient le mot "Lettings"
    """
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Lettings" in response.content


@pytest.mark.django_db
def test_lettings_detail(client):
    """
    Vérifie que la vue lettings détails fonctionne (statut 200)
    et contient le titre du Lettings
    """
    address = Address.objects.create(
        number=4, street="Privet Drive", city="Little Whinging",
        state="UK", zip_code="12345", country_iso_code="ANG"
    )
    letting = Letting.objects.create(
        title="Famille Dursley", address=address
    )

    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Famille Dursley" in response.content


@pytest.mark.django_db
def test_lettings_detail_ko(client):
    """
    Vérifie que la vue lettings détails renvoie une erreur si non trouvé
    """
    url = reverse("lettings:letting", args=[9999])
    response = client.get(url)
    assert response.status_code == 404
    assert b"Mauvais chemin O_o" in response.content
