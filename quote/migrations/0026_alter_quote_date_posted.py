# Generated by Django 4.1.1 on 2022-10-26 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0025_alter_quote_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 21, 36, 28, 855436), null=True),
        ),
    ]
