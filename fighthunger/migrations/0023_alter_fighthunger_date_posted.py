# Generated by Django 4.1.1 on 2022-11-10 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighthunger', '0022_alter_fighthunger_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighthunger',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 10, 10, 59, 37, 999429), null=True),
        ),
    ]
