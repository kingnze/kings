# Generated by Django 4.1.1 on 2022-10-26 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatevictims', '0008_alter_climatevictims_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climatevictims',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 22, 11, 0, 849226), null=True),
        ),
    ]
