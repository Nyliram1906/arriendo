# Generated by Django 5.1 on 2024-08-14 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0002_inmuebles_id_comuna_inmuebles_id_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_tipo_user',
            field=models.IntegerField(default=0),
        ),
    ]
