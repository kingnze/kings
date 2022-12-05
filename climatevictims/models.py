from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from .validators import Climatevictims_v
from datetime import datetime




class Climatevictims(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    intention1 = models.CharField(max_length=50)
    intention2 = models.CharField(max_length=50)
    intention3 = models.CharField(max_length=50)
    intention4 = models.CharField(max_length=50)
    climatevictimsimg = models.ImageField(default='climatevictimsimg.jpg',null=True,blank=True)
    climatevictimsimg_1 = models.ImageField(null=True,blank=True)
    video = models.FileField(default='video.mp4',validators=[Climatevictims_v],null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    body = RichTextField(null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Climatevictims, self).save(*args, **kwargs)
    

    class Meta:
        db_table = 'climatevictims'
        managed = True
        verbose_name = 'climatevictims'
        verbose_name_plural = 'climatevictims' 

