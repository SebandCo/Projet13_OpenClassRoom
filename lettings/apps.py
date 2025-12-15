"""
Module apps.py de la partie lettings du site

Ce module définit la configuration de l'application "lettings".
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration de l'application lettings.

    Attributes:
        name (str): Nom de l'application enregistré par Django
    """
    name = 'lettings'
