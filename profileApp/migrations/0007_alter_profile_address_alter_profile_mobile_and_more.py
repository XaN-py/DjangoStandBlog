# Generated by Django 4.1.1 on 2022-10-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
    ]
