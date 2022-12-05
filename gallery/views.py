from django.shortcuts import render
from .models import Gallery
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    gimg = Gallery.objects.order_by('-date_posted').filter(published=True)
    paginator = Paginator(gimg, 5)
    page = request.GET.get('page')
    paged_gimg = paginator.get_page(page)
    context = {'gallery':paged_gimg}
    return render(request,'gallery/gallery.html',context)
