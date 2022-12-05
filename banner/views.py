from django.shortcuts import render
from . models import Banner
# Create your views here.

def index(request):
    banner = Banner.objects.order_by('-date_posted').filter(published=True)
    context = {
        'Banner': banner
        }
    return render (request, 'banner/banner.html',context)