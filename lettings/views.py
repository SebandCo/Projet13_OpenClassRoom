"""
Module views.py de la partie lettings du site

Ce module contient les vues concernant la base de données des lettings.
Il gère :
- la page d'index de l'ensemble des lettings
- la page de détail d'un letting spécifique
"""

from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la page d'index de l'ensemble des lettings

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur

    Returns:
        HttpResponse : Réponse contenant vers le templates "lettings/index.html"
    """
    logger.info("Affichage de la page index de Lettings")
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Affiche la page de détail d'un letting

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur
        letting_id (int) : Identifiant unique du letting choisi par l'utilisateur

    Returns:
        HttpResponse : Réponse contenant le rendu du templates "lettings/letting.html"
    """
    logger.info(f"Affichage du letting id={letting_id}")
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
