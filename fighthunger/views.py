from django.shortcuts import render
from . models import Fighthunger
from blog.models import Blog
from blog.views import Blog

def index(request):
    fighthunger = Fighthunger.objects.order_by('-date_posted').filter(published=True)
    context = {
        'fighthunger': fighthunger
        }
    return render(request,'fighthunger/fighthunger.html',context)  


def fighthunger(request,slug_id):
    fighthunger = Fighthunger.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': fighthunger,
        'blog': blog
    } 
    return render(request,'fighthunger/fightinghunger.html',context)    