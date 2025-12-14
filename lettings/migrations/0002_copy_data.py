from django.db import migrations


# Préparation de la migration d'Address et Lettings
def copy_data(apps, schema_editor):
    # Récupération des anciens modèles depuis oc_lettings_site
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
        )


# Définition de la Migration
class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_data)
    ]
