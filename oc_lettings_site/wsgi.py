"""
Module wsgi.py du projet oc_lettings_site

Configure l'interface WSGI pour le projet Django à destination des serveurs compatibles WSGI
(Web Server Gateway Interface)
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
