# Generated by Django 4.1.1 on 2022-10-12 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatevictims', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='climatevictims',
            name='slug',
            field=models.SlugField(blank=True, max_length=550, null=True),
        ),
        migrations.AlterField(
            model_name='climatevictims',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 12, 4, 6, 58, 834722), null=True),
        ),
    ]
