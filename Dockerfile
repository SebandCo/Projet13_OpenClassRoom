# Fichier de configuration de Docker

# 1 --> Déclaration de Python sur Debian Slim
FROM python:3.10-slim

# 2 --> Définition du dossier de travail
WORKDIR /app

# 3 --> Installation des dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4 --> Insallation des dépendances via requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn whitenoise

# 5 --> Copie de l'ensemble du projet
COPY . .

# 6 --> Collecte des fichiers statiques
ARG SECRET_KEY=dummy
ARG SENTRY_DSN=dummy
ENV SECRET_KEY=${SECRET_KEY}
ENV SENTRY_DSN=${SENTRY_DSN}
RUN python manage.py collectstatic --noinput

# 7 --> Exposer le port de communication
EXPOSE 8000

# 8 --> Lancement de Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]