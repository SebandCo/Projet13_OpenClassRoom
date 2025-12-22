Interfaces de programmation
===========================

L'application expose les vues Django suivantes :

Vues principales
----------------

- ``/``                     : page d’accueil
- ``/profiles/``            : liste des profils
- ``/profiles/<username>/`` : détail d’un profil
- ``/lettings/``            : liste des locations
- ``/lettings/<id>/``       : détail d’une location

Vues secondaires
----------------
- ``crash/``                : Permet d'afficher la page erreur 500
- ``sentry-debug/``         : Permet d'envoyer une erreur à Sentry

Format des réponses
-------------------

- HTML via templates Django
- Pas d'API REST
