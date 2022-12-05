from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime


# Create your models here.

class Schoolequpt(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    equptimage = models.ImageField(default='equptimage.jpg')
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

class Disabled(models.Model):
    help = models.CharField(max_length=50,null=True,blank=True)
    title = models.CharField(max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    disaimage = models.ImageField(default='disaimage.jpg')
    disaimage_1 = models.ImageField(blank=True)
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


class Sustainschool(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    sustainimage = models.ImageField(default='sustainimage.jpg')
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


class Girlstec(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    slug = models.SlugField(max_length=550, null=True,blank=True)
    girltecimage = models.ImageField(default='girltecimage.jpg')
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


class Service(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True )
    serviceimg = models.ImageField(default='serviceimg.jpg')
    serviceimg_1 = models.ImageField(null=True,blank=True )
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

        class Meta:
            db_table = 'Service'
            managed = True
            verbose_name = 'Services'
            verbose_name_plural = 'Services'


class Donate(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    donateimg = models.ImageField()
    body = models.TextField()       
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True )
    title_1 = models.CharField(max_length=50)    
    published = models.BooleanField(default=True,null=True,blank=True) 

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'donate'
        managed = True
        verbose_name = 'donates'
        verbose_name_plural = 'Donates' 


class About(models.Model):
    sub_title = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True )
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()
         

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'About'
        managed = True
        verbose_name = 'About'
        verbose_name_plural = 'About' 


class Ourvision(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()
         

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Ourvision'
        managed = True
        verbose_name = 'Ourvision'
        verbose_name_plural = 'Ourvision' 


class Ourmission(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()
         

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Ourmission'
        managed = True
        verbose_name = 'Ourmission'
        verbose_name_plural = 'Ourmission' 


class Ourvalues(models.Model):
    title = models.CharField(max_length=100)
    ourvalues = models.ImageField(True,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()
         

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Ourvalues'
        managed = True
        verbose_name = 'Ourvalues'
        verbose_name_plural = 'Ourvalues' 


class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.fullname} {self.phone}'

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts' 



class Donatebanner(models.Model):
    title = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
         

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Donatebanner'
        managed = True
        verbose_name = 'Donatebanner'
        verbose_name_plural = 'Donatebanner' 


class Enoughdonate(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=datetime.now, null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    body = RichTextField()
         

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Enoughdonate'
        managed = True
        verbose_name = 'Enoughdonate'
        verbose_name_plural = 'Enoughdonate'         