from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime


# Create your models here.class Sustainschool(models.Model):
class Sustainschool(models.Model):
    title = models.CharField(max_length=550,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    sustainimage = models.ImageField(default='sustainimage.jpg')
    sustainimage_1 = models.ImageField(True,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Sustainschool, self).save(*args, **kwargs)

        class Meta:
            db_table = 'Sustainschool'
            managed = True
            verbose_name = 'Sustainschool'
            verbose_name_plural = 'Sustainschools'            






