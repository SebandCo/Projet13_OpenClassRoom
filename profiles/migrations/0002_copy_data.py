"""
Fichier de migration créé manuellement pour copier les données Profile
de l'application oc_lettings_site vers profiles

Cette migration :
- Récupère l'ancien modèle Profile contenu dans oc_lettings_site
- Crée le modèle Profile dans profiles
"""

from django.db import migrations


# Préparation de la migration de Profile
def copy_data(apps, schema_editor):
    """
    Copie les données de l'ancien modèle vers le nouveau

    Args:
        apps (Apps): Utilitaire fourni par Django pour accéder aux modèles
            dans le contexte de la migration
        schema_editor (SchemaEditor): Utilitaire pour manipuler le schéma
            de base de données (non utilisé ici)

    Process:
        - Récupère l'ancien modèle Profile contenu dans oc_lettings_site
        - Crée le modèle Profile dans profiles
    """
    # Récupération des anciens modèles depuis oc_lettings_site
    Profiles_old = apps.get_model("oc_lettings_site", "Profile")

    # Récupération des nouveaux modèles depuis Profile
    Profiles_new = apps.get_model("profiles", "Profile")

    # Récupération des profiles
    liste_profiles = {}
    for profile in Profiles_old.objects.all():
        new_profiles = Profiles_new.objects.create(
                favorite_city=profile.favorite_city,
                user=profile.user,
        )
        liste_profiles[profile.id] = new_profiles


# Définition de la Migration
class Migration(migrations.Migration):
    """
    Migration personnalisée pour transférer les données Address et Letting

    Dependencies:
        - profiles/0001_initial
        - oc_lettings_site/0002_auto_20251214_1101

    Operations:
        - RunPython(copy_data): exécute la fonction de copie des données
    """
    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0002_auto_20251214_1101"),
    ]

    operations = [
        migrations.RunPython(copy_data)
    ]
