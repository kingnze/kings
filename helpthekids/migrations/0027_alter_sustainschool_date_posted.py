# Generated by Django 4.1.1 on 2022-11-02 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpthekids', '0026_alter_sustainschool_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sustainschool',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 12, 5, 17, 793509)),
        ),
    ]
