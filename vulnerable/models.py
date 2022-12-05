from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from .validators import vulnerable_v
from datetime import datetime

# Create your models here.

class Vulnerable(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    orphans = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    childlove = models.CharField(max_length=50)
    intention4 = models.CharField(max_length=50,null=True,blank=True)
    Vulnerableimg = models.ImageField(default='Vulnerableimg.jpg',null=True,blank=True)
    video = models.FileField(default='video.mp4',validators=[vulnerable_v],null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField(null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Vulnerable, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Vulnerable'
        managed = True
        verbose_name = 'Vulnerable'
        verbose_name_plural = 'Vulnerables' 
