from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('project/<slug:slug_id>/',views.project,name='project'),
    path('contact',views.contact,name='contact'),
    path('donate',views.donate,name='donate'),
]