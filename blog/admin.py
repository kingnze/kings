from django.contrib import admin

from .models import  Blog

@admin.register(Blog)  
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','published','date_posted', 'blogimg','blogimg_1']