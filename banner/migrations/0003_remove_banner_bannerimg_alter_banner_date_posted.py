# Generated by Django 4.1.1 on 2022-10-10 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_banner_bannerimg_alter_banner_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='bannerimg',
        ),
        migrations.AlterField(
            model_name='banner',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 9, 34, 52, 643342), null=True),
        ),
    ]