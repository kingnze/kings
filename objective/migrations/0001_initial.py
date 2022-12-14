# Generated by Django 4.1.1 on 2022-10-04 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=550, null=True)),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 4, 21, 12, 50, 697140), null=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Objectives',
                'verbose_name_plural': 'Objectives',
                'db_table': 'Objective',
                'managed': True,
            },
        ),
    ]
