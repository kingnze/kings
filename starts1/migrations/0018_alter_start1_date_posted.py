# Generated by Django 4.1.1 on 2022-10-26 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starts1', '0017_alter_start1_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start1',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 22, 39, 59, 359444), null=True),
        ),
    ]
