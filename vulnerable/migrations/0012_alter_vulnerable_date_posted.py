# Generated by Django 4.1.1 on 2022-10-17 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerable', '0011_alter_vulnerable_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerable',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 17, 20, 47, 15, 806516), null=True),
        ),
    ]
