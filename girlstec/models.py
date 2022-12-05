from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime


# Create your models here.


class Girlstec(models.Model):
    subtitle = models.CharField(max_length=50,null=True,blank=True)
    title = models.CharField(max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    girltecimage = models.ImageField(default='girltecimage.jpg',null=True,blank=True)
    girltecimage_1 = models.ImageField(null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Girlstec, self).save(*args, **kwargs)

        class Meta:
            db_table = 'Girlstec'
            managed = True
            verbose_name = 'Girlstec'
            verbose_name_plural = 'Girlstecs'  