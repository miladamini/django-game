# Generated by Django 4.2.2 on 2023-07-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_slug_lditaile_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lditaile',
            name='link',
            field=models.CharField(max_length=1000, unique=True, verbose_name='لینک'),
        ),
    ]
