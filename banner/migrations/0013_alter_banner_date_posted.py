# Generated by Django 4.1.1 on 2022-10-26 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0012_alter_banner_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 22, 39, 59, 369431), null=True),
        ),
    ]