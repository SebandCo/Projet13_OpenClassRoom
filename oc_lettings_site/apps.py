"""
Module apps.py de la partie oc_lettings_site du site

Ce module définit la configuration de l'application "oc_lettings_site".
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration de l'application oc_lettings_site.

    Attributes:
        name (str): Nom de l'application enregistré par Django
    """
    name = 'oc_lettings_site'
