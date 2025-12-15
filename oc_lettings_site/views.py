"""
Module views.py de la partie d'accueil du site

Ce module contient les vues de lancement de l'application
Il gère :
- la page d'accueil
- une page d'erreur 500 pour tester la vue
"""

from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil du site

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur

    Returns:
        HttpResponse : Réponse contenant vers le templates "index.html"
    """
    return render(request, 'index.html')


# Chemin volontairement cassé pour l'affichage de l'erreur 500
def crash_erreur_500(request):
    """
    Déclenche volontairement une erreur 500 du serveur
    Cette vue est uniquement pour tester le retour du template 500.html

    Args:
        request (HttpRequest) : Objet representant la requête HTTP saisie par l'utilisateur

    Returns:
        Exception: Erreur volontaire pour simuler un crash du serveur (erreur 500)
    """
    raise Exception("Erreur volontaire")
