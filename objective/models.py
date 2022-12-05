from django.db import models
from datetime import datetime

# Create your models here.


class Objective(models.Model):
    title = models.CharField(max_length=550,null=True,blank=True)
    body = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'Objective'
        managed = True
        verbose_name = 'Objectives'
        verbose_name_plural = 'Objectives'  