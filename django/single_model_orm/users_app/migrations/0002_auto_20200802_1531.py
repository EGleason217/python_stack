# Generated by Django 3.0.8 on 2020-08-02 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='email_address',
            new_name='email',
        ),
    ]
