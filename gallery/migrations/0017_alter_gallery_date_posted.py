# Generated by Django 4.1.1 on 2022-10-16 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0016_alter_gallery_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 16, 9, 25, 9, 551467), null=True),
        ),
    ]
