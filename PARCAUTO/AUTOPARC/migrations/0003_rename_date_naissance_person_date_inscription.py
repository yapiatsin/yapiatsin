# Generated by Django 4.1.7 on 2023-03-02 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOPARC', '0002_carburant_person_delete_enregist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='date_naissance',
            new_name='date_inscription',
        ),
    ]