# Generated by Django 4.1.1 on 2022-10-17 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disabled', '0017_alter_disabled_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disabled',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 20, 47, 15, 790504)),
        ),
    ]
