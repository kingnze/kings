# Generated by Django 4.1.1 on 2022-10-06 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 15, 24, 9, 613469)),
        ),
    ]
