# Generated by Django 2.2 on 2020-08-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_aut_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Not Entered'),
            preserve_default=False,
        ),
    ]