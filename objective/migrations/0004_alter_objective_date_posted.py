# Generated by Django 4.1.1 on 2022-10-06 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objective', '0003_alter_objective_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 6, 17, 0, 22, 391519), null=True),
        ),
    ]
