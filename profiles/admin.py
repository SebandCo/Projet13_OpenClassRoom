"""
Module admin.py de la partie profiles du site

Ce module configure l'interface d'aministration pour l'application profiles
Il permet aux modèles d'être accessible et gérables via la partie admin
"""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
