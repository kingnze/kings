from django.shortcuts import render
from . models import Disabled
from blog.models import Blog
from blog.views import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    disabled = Disabled.objects.order_by('-date_posted').filter(published=True)
    paginator = Paginator(disabled, 5)
    page = request.GET.get('page')
    paged_disabled = paginator.get_page(page) 
    context = {'disabled': paged_disabled}
    return render(request, 'disabled/disabled.html',context)



def disabled(request,slug_id):
    disabled = Disabled.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': disabled,
        'blog': blog
    } 
    return render(request,'disabled/disabled_victims.html',context)