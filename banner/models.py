from django.db import models
from .validators import Banner_v
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=1000)
    bannerimg = models.ImageField(null=True,blank=True)
    bannerima_1 = models.ImageField(null=True,blank=True)
    video = models.FileField(validators=[Banner_v],null=True,blank=True)
    body = RichTextField(null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    button = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Banner'
        managed = True
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners' 
        
