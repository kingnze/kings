# Generated by Django 4.1.1 on 2022-10-09 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objective', '0015_alter_objective_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 9, 12, 33, 27, 47331), null=True),
        ),
    ]
