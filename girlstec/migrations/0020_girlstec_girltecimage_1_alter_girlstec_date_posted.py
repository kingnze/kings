# Generated by Django 4.1.1 on 2022-10-26 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girlstec', '0019_alter_girlstec_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='girlstec',
            name='girltecimage_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='girlstec',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 22, 23, 22, 840256), null=True),
        ),
    ]
