# Generated by Django 4.1.1 on 2022-10-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogimg_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]