from django.db import models
from django.utils.text import slugify
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True )
    blogimg = models.ImageField(default='blogimg.jpg')
    blogimg_1 = models.ImageField(null=True,blank=True)
    body = RichTextField()

    def __str__(self):
        return self.body

    def save(self,*args,**kwargs):
        self.slug = slugify(self.body)
        super(Blog, self).save(*args, **kwargs)

        class Meta:
            db_table = 'Blog'
            managed = True
            verbose_name = 'Blogs'
            verbose_name_plural = 'Blogs'

        