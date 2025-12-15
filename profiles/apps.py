"""
Module apps.py de la partie profiles du site

Ce module définit la configuration de l'application "profiles".
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration de l'application profiles.

    Attributes:
        name (str): Nom de l'application enregistré par Django
    """
    name = 'profiles'
