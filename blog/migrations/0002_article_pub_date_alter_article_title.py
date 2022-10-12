# Generated by Django 4.1.1 on 2022-10-07 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 7, 17, 26, 40, 756072, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(choices=[('a', 'Python'), ('b', 'Django')], max_length=150),
        ),
    ]