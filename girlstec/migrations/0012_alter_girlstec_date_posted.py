# Generated by Django 4.1.1 on 2022-10-12 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girlstec', '0011_alter_girlstec_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girlstec',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 12, 4, 6, 58, 818736), null=True),
        ),
    ]