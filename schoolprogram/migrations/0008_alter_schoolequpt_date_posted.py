# Generated by Django 4.1.1 on 2022-10-08 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolprogram', '0007_alter_schoolequpt_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolequpt',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 8, 10, 30, 30, 375400)),
        ),
    ]
