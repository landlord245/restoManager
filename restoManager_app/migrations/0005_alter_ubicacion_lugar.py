# Generated by Django 5.0.1 on 2024-05-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoManager_app', '0004_alter_ubicacion_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='lugar',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
