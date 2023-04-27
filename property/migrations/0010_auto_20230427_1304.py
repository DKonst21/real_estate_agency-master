# Generated by Django 2.2.24 on 2023-04-27 10:04

from django.db import migrations


def add_owner_records(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.iterator():
        owner_records, *_ = Owner.objects.get_or_create(
            name=flat.owner,
            phone_number=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone,
            )
        owner_records.flats.add(flat)
        owner_records.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(add_owner_records)
    ]