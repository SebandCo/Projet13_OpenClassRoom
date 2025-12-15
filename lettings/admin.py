"""
Module admin.py de la partie lettings du site

Ce module configure l'interface d'aministration pour l'application lettings
Il permet aux modèles d'être accessible et gérables via la partie admin
"""

from django.contrib import admin

from .models import Letting
from .models import Address


admin.site.register(Letting)
admin.site.register(Address)
