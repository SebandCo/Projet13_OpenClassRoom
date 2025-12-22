Déploiement et CI/CD
====================

Pipeline GitHub Actions
-----------------------

Le pipeline CI/CD comporte trois phases :

- Job 1 : **Tests**         : Exécution des tests, flake8 et couverture
- Job 2 : **Build Docker**  : Construction et push de l'image sur Docker Hub
- Job 3 : **Déploiement**   : Appel du webhook Render

Conteneurisation Docker
-----------------------

- Image basée sur ``python:3.10-slim``
- Collecte des fichiers statiques via ``collectstatic``
- Gunicorn pour le serveur WSGI
- Variables d'environnement injectées au runtime

Déploiement Render
------------------

- Service Web configuré avec : 
    ``SECRET_KEY``
    ``SENTRY_DSN``
- Déploiement déclenché par webhook
- URL publique : ``https://projet13-openclassroom.onrender.com``
