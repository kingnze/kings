from django.shortcuts import render
from . models import Schoolequpt
from blog.models import Blog
from blog.views import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    schoolequpt = Schoolequpt.objects.order_by('-date_posted').filter(published=True)
    paginator = Paginator(schoolequpt, 5)
    page = request.GET.get('page')
    paged_schoolequpt = paginator.get_page(page) 
    context = {'schoolequpt': paged_schoolequpt}
    return render(request,'schoolprogram/schoolprogram.html',context)



def school(request,slug_id):
    school = Schoolequpt.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': school,
        'blog': blog
    } 
    return render(request,'schoolprogram/ruralprogram.html',context)