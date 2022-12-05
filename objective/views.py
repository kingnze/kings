from django.shortcuts import render
from . models import Objective
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request):
    objective = Objective.objects.order_by('-date_posted').filter(is_published=True)
    paginator = Paginator(objective, 6)
    page = request.GET.get('page')
    paged_objective = paginator.get_page(page) 
    context = {'objective': paged_objective}
    return render(request,'objective/objective.html',context)  
