# Generated by Django 4.1.1 on 2022-10-25 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0024_alter_quote_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 25, 11, 43, 43, 151223), null=True),
        ),
    ]