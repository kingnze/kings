# Generated by Django 4.1.1 on 2022-10-27 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starts', '0020_alter_start_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 27, 9, 40, 58, 290662), null=True),
        ),
    ]
