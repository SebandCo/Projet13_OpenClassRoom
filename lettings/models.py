"""
Module models.py de la partie lettings du site

Ce module définit les modèles de données pour l'application lettings :
- Address : représente une adresse postale
- Letting : représente une location liée à une adresse
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale

    Attributes :
        number (int) = Numéro de la rue (valeur positive, max 9999)
        street (str) = Nom de la rue (max 64 caractères)
        city (str) = Nom de la commune (max 64 caractères)
        state (str) = Code de l'état (min 2 caractères)
        zip_code (int) = Code postal (valeur positive, max 99999)
        country_iso_code (str) = Code ISO du pays (min 3 caractères)
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Retourne une représentation de Address

        Returns:
            str : Numéro et nom de la rue
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Métadonnées de Address.

        Attributes
            verbose_name (str) : Affichage au singulier dans admin
            verbose_name_plural (str) : Affichage au pluriel dans admin
        """
        verbose_name = "Address"
        verbose_name_plural = "Address"


class Letting(models.Model):
    """
    Modèle représentant une location

    Attributes :
        title (str) = Titre de la location (max 256 caractères)
        address (str) = Adresse associée à la location (relation OneToOne avec Address)
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne une représentation de Lettings

        Returns:
            str : Titre de la location
        """
        return self.title

    class Meta:
        """
        Métadonnées de Lettings.

        Attributes
            verbose_name (str) : Affichage au singulier dans admin
            verbose_name_plural (str) : Affichage au pluriel dans admin
        """
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"
