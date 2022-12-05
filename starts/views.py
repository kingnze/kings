from django.shortcuts import render
from . models import Start
# Create your views here.


def index(request):
    starts = Start.objects.order_by('-date_posted').filter(is_published=True)
    context = {
        'starts': starts
        }

    return render(request, 'starts/starts.html',context)  