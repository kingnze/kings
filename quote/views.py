from django.shortcuts import render
from . models import Quote
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request):
    quote = Quote.objects.order_by('-date_posted').filter(is_published=True)
    paginator = Paginator(quote, 15)
    page = request.GET.get('page')
    paged_quote = paginator.get_page(page) 
    context = {'quote': paged_quote}
    return render(request,'quote/quote.html',context)  
