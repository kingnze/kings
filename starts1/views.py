from django.shortcuts import render
from . models import Start1
# Create your views here.


def index(request):
    start1 = Start1.objects.order_by('-date_posted').filter(is_published=True)
    context = {
        'start1': start1
        }

    return render(request, 'starts1/starts1.html',context)  