# Generated by Django 4.1.1 on 2022-10-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0003_alter_profile_type_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type_work',
            field=models.ManyToManyField(to='profileApp.typework'),
        ),
    ]
