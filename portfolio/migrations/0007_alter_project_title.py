# Generated by Django 3.2 on 2021-05-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210430_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Title',
            field=models.CharField(max_length=50),
        ),
    ]