# Generated by Django 4.2.2 on 2023-07-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_lditaile_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemode',
            name='img',
            field=models.ImageField(default=2, upload_to='img', verbose_name='عکس'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamemode',
            name='my_id',
            field=models.IntegerField(default=0, verbose_name='شماره'),
        ),
    ]