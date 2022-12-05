from django.shortcuts import render
from . models import Vulnerable
from blog.models import Blog
from blog.views import Blog

def index(request):
    vulnerable = Vulnerable.objects.order_by('-date_posted').filter(published=True)
    context = {
        'vulnerable': vulnerable
        }
    return render(request,'vulnerable/vulnerable.html',context)  



def vulnerablechild(request,slug_id):
    vulnerablechild = Vulnerable.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': vulnerablechild,
        'blog': blog
    } 
    return render(request,'vulnerable/vulnerablechild.html',context)