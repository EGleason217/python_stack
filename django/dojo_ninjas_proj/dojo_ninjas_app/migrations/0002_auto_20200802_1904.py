# Generated by Django 3.0.8 on 2020-08-02 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.Dojos'),
        ),
    ]
