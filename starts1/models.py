from django.db import models
from datetime import datetime

class Start1(models.Model):
    sub_title = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
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
        return self.number_1

    class Meta:
        db_table = 'Start1'
        managed = True
        verbose_name = 'Start1'
        verbose_name_plural = 'Start1' 
