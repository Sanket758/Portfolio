# Generated by Django 3.2 on 2021-04-30 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
