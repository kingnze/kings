from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import *
from objective . models import *
from quote . models import *
from blog . models import *
from banner . models import *
from schoolprogram . models import *
from helpthekids . models import *
from gallery . models import *
from girlstec . models import *
from childlove . models import *
from starts . models import *
from starts1 . models import *
from vulnerable . models import *
from fighthunger . models import *
from climatevictims . models import *
from django.contrib import messages

def index(request): 
    about = About.objects.get(pk=1)
    banner = Banner.objects.order_by('-date_posted').filter(published=True)
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:3]
    quote = Quote.objects.order_by('-date_posted').filter(is_published=True)[:3]
    objective = Objective.objects.order_by('-date_posted').filter(is_published=True)[:3]
    disabled = Disabled.objects.order_by('-date_posted').filter(published=True)[:1]
    schoolequpt = Schoolequpt.objects.order_by('-date_posted').filter(published=True)[:2]
    sustainschool = Sustainschool.objects.order_by('-date_posted').filter(published=True)[:1]
    gimg = Gallery.objects.order_by('-date_posted').filter(published=True)[:4]
    girlstec = Girlstec.objects.order_by('-date_posted').filter(published=True)[:1]
    childlove = Childlove.objects.order_by('-date_posted').filter(is_published=True)
    starts = Start.objects.order_by('-date_posted').filter(is_published=True)
    start1 = Start1.objects.order_by('-date_posted').filter(is_published=True)
    vulnerable = Vulnerable.objects.order_by('-date_posted').filter(published=True)
    fighthunger = Fighthunger.objects.order_by('-date_posted').filter(published=True)
    climatevictims = Climatevictims.objects.order_by('-date_posted').filter(published=True)
    donate_1 = Donate.objects.order_by('-date_posted').filter(published=True)

    context ={
        'about': about,
        'banner': banner,
        'blog': blog,
        'quote': quote,
        'objective': objective,
        'disabled': disabled,
        'schoolequpt': schoolequpt,
        'sustainschool': sustainschool,
        'gimg': gimg,
        'girlstec': girlstec,
        'childlove': childlove,
        'starts': starts,
        'start1': start1,
        'vulnerable': vulnerable,
        'fighthunger': fighthunger,
        'climatevictims': climatevictims,
        'donate_1': donate_1
    }

    return render(request, 'ngo/index.html',context)

def about(request):
    starts = Start.objects.order_by('-date_posted').filter(is_published=True)
    about = About.objects.order_by('-date_posted').filter(published=True)
    ourvision = Ourvision.objects.order_by('-date_posted').filter(published=True)
    ourmission = Ourmission.objects.order_by('-date_posted').filter(published=True)
    ourvalues = Ourvalues.objects.order_by('-date_posted').filter(published=True)
    childlove = Childlove.objects.order_by('-date_posted').filter(is_published=True)
    context ={
        'starts': starts,
        'childlove': childlove,
        'about': about,
        'ourvision': ourvision,
        'ourmission': ourmission,
        'ourvalues': ourvalues,
    }

    return render(request, 'ngo/about.html',context)    

def projects(request):
    project = Service.objects.order_by('-date_posted').filter(published=True)
    paginator = Paginator(project, 6)
    page = request.GET.get('page')
    paged_project = paginator.get_page(page) 
    context = {
        'project': paged_project
        }
    return render(request, 'ngo/projects.html',context)

def project(request,slug_id):
    project = Service.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:4]
    
    context = {
        'post': project,
        'blog': blog
    } 
    return render(request,'ngo/project.html',context)

def donate(request):
    donatebanner = Donatebanner.objects.order_by('-date_posted').filter(published=True)
    enoughdonate = Enoughdonate.objects.order_by('-date_posted').filter(published=True)
    starts = Start.objects.order_by('-date_posted').filter(is_published=True)
    start1 = Start1.objects.order_by('-date_posted').filter(is_published=True)
    context ={
        'donatebanner': donatebanner,
        'enoughdonate': enoughdonate,
        'starts': starts,
        'start1': start1,
    }


    return render(request, 'ngo/donate.html',context)

def contact(request):
  if request.method == 'POST':
    
      try:
          connect = Contact(fullname=request.POST['fullname'],phone=request.POST['phone'],email=request.POST['email'],message=request.POST['message'])
          messages.success(request,f"{request.POST['fullname']} Sent Successfully!!")

          connect.save()
          return redirect('contact')

      except Exception as e:
          messages.error(request,f"Something went wrong...")

  return render(request, 'ngo/contact.html')   


 