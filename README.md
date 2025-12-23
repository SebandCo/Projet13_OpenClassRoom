# Projet13_OpenClassRoom
Projet13 d'OpenClassRoom dans le cadre de la formation OpenClassRoom developpeur d'application Python

# Descriptif
Modernisation, conteneurisation et déploiement d’une application Django existante
Le projet inclut :
- refactorisation du code
- mise en place d’une architecture détaillé
- intégration d’une CI/CD complète
- création d’une image Docker reproductible
- déploiement automatisé sur Render
- documentation technique publiée sur Read the Docs

## Table des Matières
1. [Installation](#Installation)
2. [Exécution locale](#Exécution-locale)
3. [Docker](#Docker)
4. [CI/CD](#CICD)
5. [Déploiement](#Déploiement)
6. [Documentation](#Documentation)
7. [Contribution](#Contribution)

# Installation

## Pré-requis
- Python 3.10  
- pip  
- virtualenv  
- Git  
- Docker

## Création de l’environnement
Créer un environnement virtuel :
```
$ python -m venv env
```
Mettez vous dans l'environnement 
```
$ env/Scripts/activate  # Windows
$ source env/bin/activate   # macOS / Linux
```
A l'intérieur de l'environnement installer les packages
```
$ pip install -r requirements.txt
```

# Exécution locale

## Variables d’environnement
L’application nécessite :

- `SECRET_KEY`  
- `SENTRY_DSN` (optionnel en local)

A définir dans le fichier config_secret.py à créer à la racine du projet

## Lancer le serveur Django
```
python manage.py  runserver
```
Aller sur :  
http://localhost:8000

# Docker

## Construire l’image
```
$ docker build -t projet13
```

## Lancer la conteneurisation
```
$ docker run -p 8000:8000 projet13
```
L’application est accessible sur :  
http://localhost:8000

# CI/CD

Une pipeline GitHub Actions est configurée pour :

1. **Tests & Linting**  
   - pytest  
   - coverage  
   - flake8  

2. **Build Docker**  
   - construction de l’image  
   - push automatique sur Docker Hub  

3. **Déploiement Render**  
   - déclenché via webhook  
   - déploiement automatisé de la dernière image Docker  

# Déploiement

L’application est déployée sur Render :  
https://projet13-openclassroom.onrender.com

Le service Render utilise :
- Gunicorn pour le serveur WSGI  
- Whitenoise pour les fichiers statiques  
- Variables d’environnement sécurisées  
- L’image Docker publiée sur Docker Hub  

# Documentation

La documentation technique complète (installation, modèles, API, déploiement, maintenance) est disponible sur Read the Docs :

https://projet13-openclassroom.readthedocs.io

# Contribution

Commençant en programmation Python, je suis preneur :
1. des détections de bug
2. des suggestions d'améliorations du code  
3. des suggestions d'optimisations Docker  
4. des suggestions d'améliorations de la documentation  
5. des suggestions d'idées pour enrichir la CI/CD  









# Démo_en_ligne

Application déployée :
    https://projet13-openclassroom.onrender.com

Documentation technique :
    https://projet13-openclassroom.readthedocs.io

Image Docker Hub:
    https://hub.docker.com/r/sebandco/projet13_openclassroom



- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.10 ou supérieure
- Compte Sentry (pour la partie developpement)

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/SebandCo/Projet13_OpenClassRoom.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Mise en place de Sentry
Le programme est relié à Sentry pour la journalisation
Commencé par créez votre compte sur Sentry.io
Une fois le DSN récupéré
- Créér un fichier config_secret.py à la racine du projet
- Ecrire dans le fichier 
```
SENTRY_DSN = "DSN récupéré sur Sentry.io"
```

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
- Il est possible de tester la communication avec Sentry via `http://localhost:8000/sentry-debug/`

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
