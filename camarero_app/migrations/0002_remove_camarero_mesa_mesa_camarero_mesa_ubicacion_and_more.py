# Generated by Django 5.0.1 on 2024-05-18 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camarero_app', '0001_initial'),
        ('restoManager_app', '0005_alter_ubicacion_lugar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camarero_mesa',
            name='mesa',
        ),
        migrations.AddField(
            model_name='camarero_mesa',
            name='ubicacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restoManager_app.ubicacion'),
        ),
        migrations.AlterField(
            model_name='camarero_mesa',
            name='camarero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restoManager_app.camarero'),
        ),
        migrations.AlterField(
            model_name='camarero_mesa',
            name='numero_mesa',
            field=models.IntegerField(null=True),
        ),
    ]