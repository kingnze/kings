# Generated by Django 4.1.1 on 2022-11-10 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childlove', '0024_alter_childlove_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childlove',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 10, 8, 30, 1, 690139), null=True),
        ),
    ]
