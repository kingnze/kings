# Generated by Django 4.1.1 on 2022-09-28 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 28, 11, 16, 48, 838538), null=True),
        ),
    ]