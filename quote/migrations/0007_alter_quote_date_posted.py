# Generated by Django 4.1.1 on 2022-10-07 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0006_alter_quote_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 7, 8, 8, 27, 373071), null=True),
        ),
    ]
