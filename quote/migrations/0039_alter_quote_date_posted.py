# Generated by Django 4.1.1 on 2022-11-11 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0038_alter_quote_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 11, 8, 35, 40, 749605), null=True),
        ),
    ]