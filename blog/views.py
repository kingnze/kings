from django.shortcuts import render
from . models import Blog
from ngo.models import Service
from ngo.views import Service
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request):
    blog = Blog.objects.order_by('-date_posted').filter(published=True)
    paginator = Paginator(blog, 6)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page) 
    context = {'blog': paged_blog}
    return render(request,'blog/blog.html',context)



def blog(request,slug_id):
    blog = Blog.objects.filter(slug=slug_id).first()
    project = Service.objects.order_by('-date_posted').filter(published=True)[:15]
    
    context = {
        'post': blog,
        'project': project
    } 
    return render(request,'blog/blog_post.html',context)