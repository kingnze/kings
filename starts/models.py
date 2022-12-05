from django.db import models
from datetime import datetime


# Create your models here.


class Start(models.Model):
    title = models.CharField(max_length=550)
    body = models.TextField()
    startimg = models.ImageField(default='startimg.jpg',null=True,blank=True)
    number_1 = models.CharField(max_length=50,null=True,blank=True)
    name_1 = models.CharField(max_length=100,null=True,blank=True)
    number_2 = models.CharField(max_length=50,null=True,blank=True)
    name_2 = models.CharField(max_length=100,null=True,blank=True)
    number_3 = models.CharField(max_length=50,null=True,blank=True)
    name_3 = models.CharField(max_length=100,null=True,blank=True)
    number_4 = models.CharField(max_length=50,null=True,blank=True)
    name_4 = models.CharField(max_length=100,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Start'
        managed = True
        verbose_name = 'Start'
        verbose_name_plural = 'Starts'  