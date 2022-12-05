from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from .validators import fighthunger_v
from datetime import datetime
# Create your models here.


class Fighthunger(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    fighthungerimg = models.ImageField(default='fighthungerimg.jpg',null=True,blank=True)
    video = models.FileField(default='video.mp4',validators=[fighthunger_v],null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    body = RichTextField(null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Fighthunger, self).save(*args, **kwargs)    

    class Meta:
        db_table = 'Fighthunger'
        managed = True
        verbose_name = 'Fighthunger'
        verbose_name_plural = 'Fighthungers' 
