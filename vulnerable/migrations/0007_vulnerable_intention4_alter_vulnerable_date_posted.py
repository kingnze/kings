# Generated by Django 4.1.1 on 2022-10-10 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerable', '0006_alter_vulnerable_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerable',
            name='intention4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vulnerable',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 9, 34, 52, 635314), null=True),
        ),
    ]
