# Generated by Django 4.1.1 on 2022-11-10 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0028_alter_gallery_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 10, 8, 22, 46, 888289), null=True),
        ),
    ]