# Generated by Django 5.0.1 on 2024-03-08 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restoManager_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviejemplo',
            old_name='Camarero',
            new_name='camarero',
        ),
    ]
