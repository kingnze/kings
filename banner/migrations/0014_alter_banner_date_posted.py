# Generated by Django 4.1.1 on 2022-10-26 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0013_alter_banner_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 23, 12, 16, 976706), null=True),
        ),
    ]
