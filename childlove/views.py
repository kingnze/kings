from django.shortcuts import render
from . models import Childlove

# Create your views here.

def index(request):
    childlove = Childlove.objects.order_by('-date_posted').filter(is_published=True)
    context = {
        'childlove': childlove
        }
    return render(request, 'childlove/childlove.html',context)  