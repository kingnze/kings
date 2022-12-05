from django.shortcuts import render
from . models import Sustainschool
from blog.models import Blog
from blog.views import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    sustainschool = Sustainschool.objects.order_by('-date_posted').filter(published=True)
    paginator = Paginator(sustainschool, 5)
    page = request.GET.get('page')
    paged_sustainschool = paginator.get_page(page) 
    context = {'sustainschool': paged_sustainschool}
    return render(request, 'helpthekids/helpthekids.html',context)


def sustainschool(request,slug_id):
    sustainschool = Sustainschool.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': sustainschool,
        'blog': blog
    } 
    return render(request,'helpthekids/sustainschool.html',context)