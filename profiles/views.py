"""
Module views.py de la partie profiles du site

Ce module contient les vues concernant la base de données des profiles.
Il gère :
- la page d'index de l'ensemble des profiles
- la page de détail d'un profile spécifique
"""

from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Affiche la page d'index de l'ensemble des profiles

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur

    Returns:
        HttpResponse : Réponse contenant vers le templates "profiles/index.html"
    """
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
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
