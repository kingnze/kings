# Generated by Django 4.1.1 on 2022-10-16 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighthunger', '0006_alter_fighthunger_body_alter_fighthunger_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighthunger',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 16, 9, 25, 9, 575481), null=True),
        ),
    ]