"""
Fichier de migration créé manuellement pour copier les données Address et Letting
de l'application oc_lettings_site vers lettings

Cette migration :
- Récupère les anciens modèle Address et Letting contenu dans oc_lettings_site
- Crée les modèles Address et Letting dans lettings
- Conserve les relations entre Letting et Address
"""
from django.db import migrations


# Préparation de la migration d'Address et Lettings
def copy_data(apps, schema_editor):
    """
    Copie les données des anciens modèles vers les nouveaux

    Args:
        apps (Apps): Utilitaire fourni par Django pour accéder aux modèles
            dans le contexte de la migration
        schema_editor (SchemaEditor): Utilitaire pour manipuler le schéma
            de base de données (non utilisé ici)

    Process:
        - Récupère les modèles Address et Letting depuis oc_lettings_site
        - Récupère les modèles Address et Letting depuis lettings
        - Recrée les relations entre Letting et Address et recrée les liens entre chaque instance
    """
    # Neutralisation de la migration car provoque des erreurs lors des tests
    # Migration sans interet une fois que les données ont été transféré
    pass
    
    """# Récupération des anciens modèles depuis oc_lettings_site
    Addresse_old = apps.get_model("oc_lettings_site", "Address")
    Letting_old = apps.get_model("oc_lettings_site", "Letting")

    # Récupération des nouveaux modèles depuis lettings
    Addresse_new = apps.get_model("lettings", "Address")
    Letting_new = apps.get_model("lettings", "Letting")

    # Récupération des adresses
    liste_adress = {}
    for address in Addresse_old.objects.all():
        new_address = Addresse_new.objects.create(
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code,
        )
        liste_adress[address.id] = new_address

    # Récupération des lettings
    # Pas de dictionnaire car address de lettings est lié à Address
    for letting in Letting_old.objects.all():
        Letting_new.objects.create(
            title=letting.title,
            address=liste_adress[letting.address.id],
        )"""


# Définition de la Migration
class Migration(migrations.Migration):
    """
    Migration personnalisée pour transférer les données Address et Letting

    Dependencies:
        - lettings/0001_initial
        - oc_lettings_site/0001_initial

    Operations:
        - RunPython(copy_data): exécute la fonction de copie des données
    """
    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_data)
    ]
