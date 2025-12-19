"""
Module views.py de la partie profiles du site

Ce module contient les vues concernant la base de données des profiles.
Il gère :
- la page d'index de l'ensemble des profiles
- la page de détail d'un profile spécifique
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la page d'index de l'ensemble des profiles

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur

    Returns:
        HttpResponse : Réponse contenant vers le templates "profiles/index.html"
    """
    logger.info("Affichage de la page index de Profiles")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche la page de détail d'un profile

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur
        profile_id (int) : Identifiant unique du profile choisi par l'utilisateur

    Returns:
        HttpResponse : Réponse contenant le rendu du templates "profiles/profile.html"
        HttpResponse : Réponse page 404 si le profile n'existe pas
    """
    logger.info(f"Affichage du profil : {username}")
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
