# Generated by Django 4.1.1 on 2022-11-02 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0016_alter_banner_date_posted_alter_banner_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 12, 5, 17, 824749), null=True),
        ),
    ]
