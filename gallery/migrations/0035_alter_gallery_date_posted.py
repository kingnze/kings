# Generated by Django 4.1.1 on 2022-12-05 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0034_alter_gallery_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 5, 14, 18, 0, 737221), null=True),
        ),
    ]
