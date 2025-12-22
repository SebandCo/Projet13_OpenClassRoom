Démarrage
=========

Lancer le serveur Django
------------------------

.. code-block:: bash

    python manage.py runserver

Lancer les tests
----------------

.. code-block:: bash

    pytest --cov=.

Construire l’image Docker
-------------------------

.. code-block:: bash

    docker build -t projet13 .

Lancer le conteneur
-------------------

.. code-block:: bash
    
    docker run -p 8000:8000 projet13
