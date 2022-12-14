# Generated by Django 4.1.1 on 2022-10-25 10:43

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('date_posted', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('serviceimg', models.ImageField(default='serviceimg.jpg', upload_to='')),
                ('serviceimg_1', models.ImageField(upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
