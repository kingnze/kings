# Generated by Django 4.1.1 on 2022-11-11 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0022_alter_banner_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 11, 8, 35, 40, 820079), null=True),
        ),
    ]
