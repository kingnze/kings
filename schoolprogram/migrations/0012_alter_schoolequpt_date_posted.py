# Generated by Django 4.1.1 on 2022-10-09 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolprogram', '0011_alter_schoolequpt_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolequpt',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 9, 12, 33, 27, 49330)),
        ),
    ]
