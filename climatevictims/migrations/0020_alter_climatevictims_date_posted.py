# Generated by Django 4.1.1 on 2022-11-10 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatevictims', '0019_alter_climatevictims_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climatevictims',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 10, 10, 59, 38, 36440), null=True),
        ),
    ]
