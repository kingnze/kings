# Generated by Django 4.1.1 on 2022-10-17 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]