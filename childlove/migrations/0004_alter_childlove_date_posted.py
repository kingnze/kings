# Generated by Django 4.1.1 on 2022-10-08 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childlove', '0003_alter_childlove_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childlove',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 8, 10, 30, 30, 390985), null=True),
        ),
    ]
