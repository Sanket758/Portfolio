# Generated by Django 3.2 on 2021-05-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Description',
            field=models.TextField(),
        ),
    ]
