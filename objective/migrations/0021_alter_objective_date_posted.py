# Generated by Django 4.1.1 on 2022-10-17 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objective', '0020_alter_objective_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 17, 14, 50, 27, 161267), null=True),
        ),
    ]
