"""
Module tests_urls.py de la partie profiles

Ce module teste les urls Profiles
"""

from django.urls import reverse, resolve
from profiles.views import index, profile


def test_profiles_index_url_resolves():
    """
    Vérifie que l'URL profile_index dirige bien vers la vue correspondante
    """
    url = reverse("profiles:index")
    assert resolve(url).func == index


def test_profiles_detail_url_resolves():
    """
    Vérifie que l'URL profile_detail dirige bien vers la vue correspondante
    """
    url = reverse("profiles:profile", args=["harry"])
    assert resolve(url).func == profile
