# Generated by Django 4.1.1 on 2022-10-07 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='TypeWork',
        ),
    ]
