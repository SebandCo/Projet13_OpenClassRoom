from django.db import migrations


# Préparation de la migration de Profile
def copy_data(apps, schema_editor):
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
    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0002_auto_20251214_1101"),
    ]

    operations = [
        migrations.RunPython(copy_data)
    ]
