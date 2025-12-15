"""
Module asgi.py du projet oc_lettings_site

Configure l'interface ASGI pour le projet Django à destination des serveurs compatibles ASGI
(Asynchronous Server Gateway Interface)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
