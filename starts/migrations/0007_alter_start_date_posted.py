# Generated by Django 4.1.1 on 2022-10-09 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starts', '0006_alter_start_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 9, 12, 33, 27, 61238), null=True),
        ),
    ]
