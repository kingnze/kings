# Generated by Django 4.1.1 on 2022-11-10 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolprogram', '0029_alter_schoolequpt_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolequpt',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 10, 39, 14, 671989)),
        ),
    ]
