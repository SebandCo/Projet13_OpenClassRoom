"""
Module urls.py de la partie lettings du site

Ce module définit les chemins d'accès de chaque partie de lettings.
"""

from django.urls import path
from . import views

# Listes des différentes routes lié à lettings
app_name = "lettings"

# '', views.index, name='index'
#         --> Page d'accueil de la partie lettings
# '<int:letting_id>/', views.letting, name='letting'
#         --> Page de détail d'un lettings en particulier
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
