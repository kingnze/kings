from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime

# Create your models here.

class Schoolequpt(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    equptimage = models.ImageField(default='equptimage.jpg')
    equptimage_1 = models.ImageField(True,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Schoolequpt, self).save(*args, **kwargs)

        class Meta:
            db_table = 'Schoolequpt'
            managed = True
            verbose_name = 'Schoolequpt'
            verbose_name_plural = 'Schoolequpts'
