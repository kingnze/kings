# Generated by Django 4.1.1 on 2022-11-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0007_about_ourmission_ourvalues_ourvision_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourvalues',
            name='ourvalues',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name=True),
        ),
    ]