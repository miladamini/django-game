# Generated by Django 4.2.2 on 2023-07-03 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_lditaile_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lditaile',
            old_name='slug',
            new_name='link',
        ),
    ]
