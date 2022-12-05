from django.shortcuts import render
from . models import Climatevictims
from blog.models import Blog
from blog.views import Blog

# Create your views here.

def index(request):
    climatevictims = Climatevictims.objects.order_by('-date_posted').filter(published=True)
    context = {
        'climatevictims': climatevictims
        }
    return render(request,'climatevictims/climatevictims.html',context) 


def climate(request,slug_id):
    climate = Climatevictims.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': climate,
        'blog': blog
    } 
    return render(request,'climatevictims/climate.html',context)