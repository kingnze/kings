# Generated by Django 4.1.1 on 2022-10-26 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0026_alter_quote_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 22, 11, 0, 815261), null=True),
        ),
    ]
