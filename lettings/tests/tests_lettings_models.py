"""
Module tests_models.py de la partie lettings

Ce module teste les models Address et Letting
"""
import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_retour_str():
    """
    Vérifie que __str__ d'Address retourne "number street"
    """
    address = Address.objects.create(
        number=4, street="Privet Drive", city="Little Whinging",
        state="UK", zip_code="12345", country_iso_code="ANG"
    )
    assert str(address) == "4 Privet Drive"


def test_address_verbose_name():
    """
    Vérifie les verboses_name défini pour Address
    """
    assert Address._meta.verbose_name == "Address"
    assert Address._meta.verbose_name_plural == "Address"


@pytest.mark.django_db
def test_letting_retour_str():
    """
    Vérifie que __str__ de Letting retourne "title"
    """
    address = Address.objects.create(
        number=4, street="Privet Drive", city="Little Whinging",
        state="UK", zip_code="12345", country_iso_code="ANG"
    )
    letting = Letting.objects.create(
        title="Famille Dursley", address=address
    )
    assert str(letting) == "Famille Dursley"


def test_letting_verbose_name():
    """
    Vérifie les verboses_name défini pour Letting
    """
    assert Letting._meta.verbose_name == "Letting"
    assert Letting._meta.verbose_name_plural == "Lettings"
