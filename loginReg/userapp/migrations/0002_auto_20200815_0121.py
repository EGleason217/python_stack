# Generated by Django 3.1 on 2020-08-15 01:21

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('obejects', django.db.models.manager.Manager()),
            ],
        ),
    ]
