# Generated by Django 4.1.1 on 2022-10-09 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disabled', '0010_alter_disabled_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disabled',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 9, 11, 40, 33, 594821)),
        ),
    ]