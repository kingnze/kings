# Generated by Django 4.1.1 on 2022-10-04 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 4, 21, 12, 50, 697140)),
        ),
    ]
