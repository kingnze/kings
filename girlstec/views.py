from django.shortcuts import render
from . models import Girlstec
from blog.models import Blog
from blog.views import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    girlstec = Girlstec.objects.order_by('-date_posted').filter(published=True)
    paginator = Paginator(girlstec, 5)
    page = request.GET.get('page')
    paged_girlstec = paginator.get_page(page) 
    context = {'girlstec': paged_girlstec}
    return render(request, 'girlstec/girlstec.html',context)


def girlstec(request,slug_id):
    girlstec = Girlstec.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': girlstec,
        'blog': blog
    } 
    return render(request,'girlstec/girlstec_leaning.html',context)