# Generated by Django 4.1.1 on 2022-10-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0002_profile_address_profile_mobile_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type_work',
            field=models.ManyToManyField(blank=True, null=True, to='profileApp.typework'),
        ),
    ]
