# Generated by Django 4.1.1 on 2022-10-27 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starts1', '0019_alter_start1_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start1',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 27, 9, 32, 13, 764884), null=True),
        ),
    ]
