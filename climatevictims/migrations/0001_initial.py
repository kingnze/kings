# Generated by Django 4.1.1 on 2022-10-10 08:34

import climatevictims.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climatevictims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('body', models.TextField()),
                ('intention1', models.CharField(max_length=50)),
                ('intention2', models.CharField(max_length=50)),
                ('intention3', models.CharField(max_length=50)),
                ('intention4', models.CharField(max_length=50)),
                ('climatevictimsimg', models.ImageField(blank=True, default='climatevictimsimg.jpg', null=True, upload_to='')),
                ('video', models.FileField(blank=True, default='video.mp4', null=True, upload_to='', validators=[climatevictims.validators.Climatevictims_v])),
                ('date_posted', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 9, 34, 52, 643342), null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'climatevictims',
                'verbose_name_plural': 'climatevictims',
                'db_table': 'climatevictims',
                'managed': True,
            },
        ),
    ]
