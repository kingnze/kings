# Generated by Django 4.1.1 on 2022-10-07 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpthekids', '0002_alter_sustainschool_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sustainschool',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 10, 10, 14, 537058)),
        ),
    ]