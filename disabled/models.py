from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class Disabled(models.Model):
    help = models.CharField(max_length=50,null=True,blank=True)
    title = models.CharField(max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    disaimage = models.ImageField(default='disaimage.jpg')
    disaimage_1 = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Disabled, self).save(*args, **kwargs)

        class Meta:
            db_table = 'Disabled'
            managed = True
            verbose_name = 'Disabled'
            verbose_name_plural = 'Disableds'