"""
Module models.py de la partie profiles du site

Ce module définit les modèles de données pour l'application profiles :
- Profile : représente un utilisateur du site
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant le profil d'un utilisateur

    Attributes :
        user (int) = Identifiant de l'utilisateur (relation OneToOne avec User)
        favorite_city (str) = Ville favorite de l'utilisateur (max 64 caractères, non obligatoire)
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne une représentation de Profile

        Returns:
            str : Titre de la location
        """
        return self.user.username

    class Meta:
        """
        Métadonnées de Profile.

        Attributes
            verbose_name (str) : Affichage au singulier dans admin
            verbose_name_plural (str) : Affichage au pluriel dans admin
        """
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
