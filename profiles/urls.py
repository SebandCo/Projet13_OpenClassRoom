"""
Module urls.py de la partie profiles du site

Ce module définit les chemins d'accès de chaque partie de profiles.
"""

from django.urls import path
from . import views

# Listes des différentes routes lié à profiles
app_name = "profiles"

# '', views.index, name='index'
#         --> Page d'accueil de la partie profiles
# '<str:username>/', views.profile, name='profile'
#         --> Page de détail d'un profiles en particulier
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
