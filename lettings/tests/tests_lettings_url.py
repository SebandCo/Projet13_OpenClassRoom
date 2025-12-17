"""
Module tests_urls.py de la partie lettings

Ce module teste les urls Address et Letting
"""

from django.urls import reverse, resolve
from lettings.views import index, letting


def test_lettings_index_url_resolves():
    """
    Vérifie que l'URL letting_index dirige bien vers la vue correspondante
    """
    url = reverse("lettings:index")
    assert resolve(url).func == index


def test_lettings_detail_url_resolves():
    """
    Vérifie que l'URL letting_detail dirige bien vers la vue correspondante
    """
    url = reverse("lettings:letting", args=[1])
    assert resolve(url).func == letting
