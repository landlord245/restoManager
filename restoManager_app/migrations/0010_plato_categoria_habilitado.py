# Generated by Django 5.0.1 on 2024-03-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoManager_app', '0009_plato_categoria_numero_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato_categoria',
            name='habilitado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]