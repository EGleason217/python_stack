# Generated by Django 2.2 on 2020-08-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='comment',
            field=models.TextField(default='default entry'),
            preserve_default=False,
        ),
    ]