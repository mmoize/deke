# Generated by Django 2.2.5 on 2019-09-18 09:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('sydney', django.db.models.manager.Manager()),
            ],
        ),
    ]
