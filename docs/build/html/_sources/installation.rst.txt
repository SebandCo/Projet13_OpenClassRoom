Installation
============

Prérequis
---------
- Python 3.10
- pip
- virtualenv
- Docker (optionnel pour tests)

Installation en locale
----------------------

Clonez le début :

.. code-block:: bash

    git clone https://github.com/SebandCo/Projet13_OpenClassRoom.git
    cd Projet13_OpenClassRoom

Créez un environnement virtuel :

.. code-block:: bash

    python -m venv env
    source env/bin/activate  # Windows : env\Scripts\activate

Installez les dépendances :

.. code-block:: bash

    pip install -r requirements.txt

Variables d'environnement
-------------------------

L'application nécessite : 
- ``SECRET_KEY`` : clé Django
- ``SENTRY_DSN`` : optionnel en local

Les variables sont à définir dans un fichier config_secret.py
