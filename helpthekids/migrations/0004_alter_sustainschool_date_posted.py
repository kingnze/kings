# Generated by Django 4.1.1 on 2022-10-07 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpthekids', '0003_alter_sustainschool_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sustainschool',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 10, 23, 53, 61648)),
        ),
    ]