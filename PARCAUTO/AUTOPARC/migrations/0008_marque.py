# Generated by Django 4.1.7 on 2023-03-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOPARC', '0007_alter_vehicule_vehi_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=225)),
            ],
        ),
    ]
