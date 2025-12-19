"""
Module tests_sentry.py de la partie oc_lettings_site

Ce module teste que la liaison avec Sentry fonctionne correctement
"""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_main_sentry_erreur(client):
    """
    Vérifie que la vue sentry-debug déclenche bien une exception
    En se connectant à Sentry, permet de voir si l'erreur est bien reçu
    """
    with pytest.raises(Exception):
        client.get(reverse("sentry_debug"))
