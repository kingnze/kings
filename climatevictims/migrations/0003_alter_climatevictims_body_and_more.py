# Generated by Django 4.1.1 on 2022-10-13 07:27

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatevictims', '0002_climatevictims_slug_alter_climatevictims_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climatevictims',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='climatevictims',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 8, 27, 34, 691922), null=True),
        ),
    ]