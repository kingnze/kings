# Generated by Django 4.1.1 on 2022-11-10 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starts1', '0024_start1_body_start1_sub_title_start1_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start1',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 10, 10, 39, 14, 687004), null=True),
        ),
    ]
