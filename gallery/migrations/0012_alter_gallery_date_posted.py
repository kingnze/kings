# Generated by Django 4.1.1 on 2022-10-09 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_alter_gallery_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 9, 11, 40, 33, 586868), null=True),
        ),
    ]