# Generated by Django 4.1.1 on 2022-11-10 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighthunger', '0018_alter_fighthunger_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighthunger',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 10, 8, 22, 47, 169533), null=True),
        ),
    ]
