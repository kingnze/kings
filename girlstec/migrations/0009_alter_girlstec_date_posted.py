# Generated by Django 4.1.1 on 2022-10-09 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girlstec', '0008_alter_girlstec_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girlstec',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 9, 11, 40, 33, 594821), null=True),
        ),
    ]