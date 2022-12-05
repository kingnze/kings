from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class Childlove(models.Model):
    subtitle = models.CharField(max_length=10,null=True,blank=True)
    title = models.CharField(max_length=550,null=True,blank=True)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    accordimg = models.ImageField(default='accordimg.jpg',null=True,blank=True)
    accordtitle_1 = models.CharField(max_length=550,null=True,blank=True)
    accordbody_1 = models.TextField(null=True,blank=True)
    accordtitle_2 = models.CharField(max_length=550,null=True,blank=True)
    accordbody_2 = models.TextField(null=True,blank=True)
    accordtitle_3 = models.CharField(max_length=550,null=True,blank=True)
    accordbody_3 = models.TextField(null=True,blank=True)
    accordtitle_4 = models.CharField(max_length=550,null=True,blank=True)
    accordbody_4 = models.TextField(null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Childlove, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Childlove'
        managed = True
        verbose_name = 'Childlove'
        verbose_name_plural = 'Childloves'  