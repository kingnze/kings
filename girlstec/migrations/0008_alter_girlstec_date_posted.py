# Generated by Django 4.1.1 on 2022-10-08 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girlstec', '0007_alter_girlstec_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girlstec',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 8, 11, 45, 34, 901323), null=True),
        ),
    ]
