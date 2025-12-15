"""
Script manage.py du projet Django oc_lettings_site.

Ce script est le point de départ des commandes Django.
Il permet d'excuter :
- Le lancement du serveur de développement
- Appliquer les migrations
- exécuter les tests
"""

import os
import sys


def main():
    """
    Point de départ du script manage.py

    Configure les paramètres Django par défaut et exécute la commande passée en
    argument via la ligne de commande.

    Raises:
        ImportError : Se déclenche si Django n'est pas installé dans l'environnement
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
