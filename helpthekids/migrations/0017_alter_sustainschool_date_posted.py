# Generated by Django 4.1.1 on 2022-10-17 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpthekids', '0016_alter_sustainschool_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sustainschool',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 14, 50, 27, 168058)),
        ),
    ]
