from django.db import models
from datetime import datetime


# Create your models here.

class Gallery(models.Model):
    imggallery = models.ImageField(default='imggallery.jpg')
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)

    class Meta:
        db_table = 'Gallery'
        managed = True
        verbose_name = 'Gallerys'
        verbose_name_plural = 'Gallerys'

