"""
Module tests_models.py de la partie profiles

Ce module teste les models Profiles
"""
import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_retour_str():
    """
    Vérifie que __str__ de Profile retourne "number street"
    """
    user = User.objects.create_user(username="harry", password="secret")
    profile = Profile.objects.create(user=user, favorite_city="Poudlard")
    assert str(profile) == "harry"


def test_profile_verbose_name():
    """
    Vérifie les verboses_name défini pour Profile
    """
    assert Profile._meta.verbose_name == "Profile"
    assert Profile._meta.verbose_name_plural == "Profiles"
