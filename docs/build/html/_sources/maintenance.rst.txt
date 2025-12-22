Maintenance et supervision
==========================

Tests automatisés
-----------------

Les tests sont exécutés à chaque commit via GitHub Actions

Supervision
-----------

Sentry permet de :
- Suivre les erreurs
- Analyser les performances
- Recevoir des alertes

Mises à jour
------------

- Mettre à jour les dépendances via ``pip install -U``
- Appliquer les changements via Rebuild Docker
- Déploiement Render automatisé via webhook
