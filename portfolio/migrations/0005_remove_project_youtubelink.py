# Generated by Django 3.2 on 2021-04-30 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210430_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='YoutubeLink',
        ),
    ]
